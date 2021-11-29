# pytest
from logging import getLogger as gL
LOGGER = gL(__name__)
# python native
from os.path import isdir as dirExists
# this module
from .createHugoStructure import createHugoStructure

def isFolderStructure(hugoContent: str) -> bool:
    """
    check if hugoContent folder exists
    """

    if not dirExists(hugoContent):
        LOGGER.info('Generate new Hugo content folder')
        return False
    else:
        LOGGER.info('Hugo content folder exists')
        return True
