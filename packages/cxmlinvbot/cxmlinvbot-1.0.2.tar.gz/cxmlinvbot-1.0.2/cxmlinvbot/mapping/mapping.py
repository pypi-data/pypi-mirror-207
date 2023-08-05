import logging
from   cxmlinvbot.config.base import BaseConfig

logger = logging.getLogger(__name__)


class Mapping(object):

    DTD_URL = BaseConfig.CXML_DTD_URL
    STRUCTURE = []
    FIELD_TO_ACTION_MAP = {}

    def getDTD_URL(self):
        return self.DTD_URL
    
    def getMap(self) -> dict:
        return self.FIELD_TO_ACTION_MAP
    
    def perform(self, nvPairs):
        m = {}
        for e in self.STRUCTURE:
            m[e] = None
        for fam in self.FIELD_TO_ACTION_MAPS:
            for key, action in fam.items():
                m.update(action.perform(key, nvPairs))
        return m