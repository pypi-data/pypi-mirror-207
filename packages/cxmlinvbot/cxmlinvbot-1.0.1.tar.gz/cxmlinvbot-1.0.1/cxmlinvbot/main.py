import csv
import glob
import logging
import os
import pathlib
import requests
import time
import traceback

from   cxmlinvbot.config.base import BaseConfig
from   cxmlinvbot.config.env import EnvConfig
from   cxmlinvbot.config.mail import MailConfig
from   cxmlinvbot.errors.errors import LockedFileError, MapActionError
from   cxmlinvbot.filing.filing import Archive
from   cxmlinvbot.mail.mail import Mail
from   cxmlinvbot.mapping.action import MapActionError
from   cxmlinvbot.mapping.invoicedetailrequestmapping import InvoiceDetailRequestMapping
from   cxmlinvbot.objects.cxmlobject import CXMLObject, CXML_DTDError
from   cxmlinvbot.objects.response import Response

'''
# For debugging HTTP requests
import http.client as http_client
http_client.HTTPConnection.debuglevel = 1
'''

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s : %(levelname)s : %(module)s : %(message)s')
logger = logging.getLogger(__name__)

csvArchive = Archive(EnvConfig.ACRHIVE_CSV_PATH, 'csv', EnvConfig.CLEANSE_PERIOD)
cxmlArchive = Archive(EnvConfig.ACRHIVE_CXML_PATH, 'cxml', EnvConfig.CLEANSE_PERIOD)
logArchive = Archive(EnvConfig.LOG_PATH, 'log', EnvConfig.CLEANSE_PERIOD)

mail = Mail()


def cleanseAll():
    if EnvConfig.CLEANSE_ARCHIVES:
        csvArchive.cleanse()
        cxmlArchive.cleanse()
    if EnvConfig.CLEANSE_LOGS:
        logArchive.cleanse()
    graceFiles = glob.glob('*.grace', root_dir=EnvConfig.PROJECT_FULLPATH)
    for gf in graceFiles:
        os.remove(gf)

def postCXML(invoice, cxml):
    endPoint = BaseConfig.PROD_INVOICE_END_POINT \
        if EnvConfig.TGT_ENDPOINT == 'production' else BaseConfig.TEST_INVOICE_END_POINT
    
    # Can raise ConnectionError
    headers = {'Content-Type':'text/xml'}
    r = requests.post(endPoint, headers=headers, data=cxml.asXMLString())

    logger.info('Response for cxml from endpoint - %s : %s' % (r.status_code, r.text))
    if r.status_code == 200:
        cxmlResp = Response()
        cxmlResp.fromXMLString(r.text.replace('encoding="UTF-8"', ''))
        if cxmlResp.status.code == 200:
            with cxmlArchive.createFile(invoice) as cxmlFile:
                cxmlFile.write(cxml.asXMLString(prettyPrint=True))
        else:
            return {invoice : '%s : %s : %s' % (cxmlResp.status.code, cxmlResp.status.text, cxmlResp.status.data)}
    else:
       # Raise as HTTPError
       r.raise_for_status()
    return {}

def processInvoice(row):
    invoice = row['InvoiceNumber']
    if not len(invoice):
        raise MapActionError('Data Error: InvoiceNumber field is missing from CSV can\'t do anything without this')
    
    logger.info('Processing invoice - %s' % invoice)
    if not cxmlArchive.exists(invoice):
        cxml = CXMLObject()
        req = InvoiceDetailRequestMapping()
        try:
            cxml.fromPathValueMap(req.perform(row))
            cxml.validate(req.getDTD_URL())
        except MapActionError as e1:
            logger.error('Data Error: CSV mapping failed, please correct CSV for missing fields below...')
            logger.error(e1)
            return {invoice : e1}
        except CXML_DTDError as e2:
            logger.error('Data Error: Invoice failed to validate against the DTD, this will need to be corrected...')
            logger.error(e2)  
            return {invoice : e2}
        return postCXML(invoice, cxml)
    else:
        logger.info('Seen this invoice before, will not process again')
    return {}

def mailBatchComplete(f, badInvoices):
    logger.info(MailConfig.BATCH_MAIL_TEMPLATE % (f, len(badInvoices)))
    mail.addSubject('Prodoor Invoice Bot - %s' % f)
    mail.addContent(MailConfig.BATCH_MAIL_TEMPLATE % (f, len(badInvoices)))
    for n, (i, e) in enumerate(badInvoices.items()):
        if n == 0:
            mail.addContent(MailConfig.ERROR_INTRO)
        mail.addContent(MailConfig.INVOICE_ERROR % (i, e))
    mail.send()

def mailFatal(message):
    logger.fatal(message)
    mail.addSubject('Prodoor Invoice Bot - FATAL error')
    mail.addContent('ERROR DETAILS\n')
    mail.addContent(message)
    mail.send()

def main():
    pid = os.getpid()
    logger.info('Starting ProDoor Invoice Bot...PID (%s)' % pid)
    logger.info('Running in %s deployment mode' % EnvConfig.DEPLOYMENT_MODE)

    cleanseAll()

    # Deleting the grace file will cause the bot to exit gracefully
    graceFile = '%s%s.grace' % (EnvConfig.PROJECT_FULLPATH, pid)
    pathlib.Path(graceFile).touch()

    lockedFileCountMap = {}
    try:
        while(os.path.exists(graceFile)):
            # List available csv files
            files = glob.glob('*.csv', root_dir=EnvConfig.NEW_CSV_PATH)
            for f in files:
                logger.info('Processing CSV invoice file - %s' % f)
                # TODO: may not need to do this locked file handling if the windows scheduling works as anticpiated
                lockedFileCount = lockedFileCountMap.get(f, 0)
                try:
                    csvFile = open(EnvConfig.NEW_CSV_PATH + f, newline='', encoding='utf-8-sig', mode='r+')
                except PermissionError as e:
                    # The file is locked let's go round the loop and see if it becomes unlocked
                    lockedFileCountMap[f] = lockedFileCount + 1
                    if lockedFileCount + 1 > EnvConfig.LOCKED_FILE_RETRIES:
                        raise LockedFileError('CSV file locked for over %d minutes - %s' % (EnvConfig.LOCKED_FILE_RETRIES, f))
                    logger.warning('CSV is locked by another user, will retry.')
                    continue

                badInvoices = {}
                reader = csv.DictReader(csvFile, delimiter=',')
                for row in reader:
                    badInvoices.update(processInvoice(row))
                csvFile.close()
                csvArchive.archive(EnvConfig.NEW_CSV_PATH, f)
                
                mailBatchComplete(f, badInvoices)

            time.sleep(EnvConfig.HEARTBEAT_TIME)
            logger.info('HEARTBEAT...')
        logger.info('Exiting...')
        return 0
    except LockedFileError as lfe:
        message = str(lfe)
        message += traceback.format_exc() + '\n'
        message += 'Invoice Bot has died and will be automatically restarted shortly\n'
        message += 'Please close the CSV file ASAP...'
        errorCode = 100
    except (ConnectionError, requests.HTTPError):
        message = 'Connection Error: An error occurred either connecting to or sending data to the Coupa endpoint...\n'
        message += traceback.format_exc() + '\n'
        message += 'Invoice Bot has died and will be automatically restarted shortly\n'
        message += 'If this error does not clear on restart pleace contact Coupa support...'
        errorCode = 100
    except BaseException:
        message = 'Fatal Error: An unexpected error condition occured...\n'
        message += traceback.format_exc() + '\n'
        message += 'Invoice Bot has died and will NOT be automatically restarted\n'
        message += 'Please address the above error and restart the Bot...'
        errorCode = 999
    mailFatal(message)

    return errorCode


if __name__ == '__main__':
    main()
