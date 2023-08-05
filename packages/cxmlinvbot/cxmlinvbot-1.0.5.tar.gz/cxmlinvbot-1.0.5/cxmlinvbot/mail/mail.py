import itertools
import logging
import sys
import io
import smtplib
from   datetime import datetime, timedelta

from local.config.mail import MailConfig

logger = logging.getLogger(__name__)


class Mail():
    '''
    Send emails!
    '''
    def __init__(self, subject:str=None, content:list=None):
        '''
        Initialise the Mail class with content; all parameters are optional
        and can be added instead via the Mail interface.

        :param subject: the subject line of the email
        :param content: a list of strs or files containing content
        '''
        self._container = 'MIME-Version: 1.0\nContent-type: text/html\n' \
                'Subject:{subject}\n\n{body}</body>'
        self._firstTable = True
        self._subject = ''
        self._body = ''
        self._stdRecipients = True

        self.addSubject(subject)
        self.addContent(content)

        self._sender = MailConfig.FROM
        self._recipients = MailConfig.RECIPIENTS
        self._server = smtplib.SMTP(MailConfig.SVR, MailConfig.PORT)
        if 'localhost' not in MailConfig.SVR:
            self._server.ehlo()
            self._server.starttls()
            self._server.ehlo()
            self._server.login(self._sender, MailConfig.PWD)
        
    def addSubject(self, subject:str):
        if isinstance(subject, str):
            self._subject = subject

    def addContent(self, content):
        if content:
            if isinstance(content, str):
                self._addTextContent(content)
            elif isinstance(content, io.TextIOBase):
                self._addFileContent(content)

    def addRecipients(self, recipients:list):
        for r in recipients:
            self.addRecipient(r)

    def addRecipient(self, recipient):
        if self._stdRecipients:
            self._stdRecipients = False
            self._recipients = []

        if all([x in recipient for x in ('@', '.')]):
            self._recipients.append(recipient)

    def _addTextContent(self, content):
        self._body += '{}<br/><br/>'.format(content) 

    def _addFileContent(self, content):
        self._addTextContent(content.read())

    def send(self):
       self._server.sendmail(*self._repr()) 
       logger.info('email sent to: {!s}'.format(self._recipients))
 
    def __str__(self):
        return self._container.format(subject=self._subject, body=self._body)

    def __repr__(self):
        return str(self._repr())
    
    def _repr(self):
        return (self._sender, self._recipients, str(self))


if __name__ == '__main__':
    mail = Mail()
    mail.addSubject('Prodoor Invoice Bot - information')
    mail.addContent('Hello World')
    mail.send()
