from .checkHugoCommand import isHugoAvailable
from os import system as runCommand
from logging import getLogger as gL
LOGGER = gL(__name__)

def runHugoStructure(hugoFolder: str):
    """
    Run Hugo command to create a new site folder
    """

    # precondition
    assert isinstance(hugoFolder, str), 'hugoFolder no es un string'

    # logic
    if isHugoAvailable():
        runCommand("hugo new site %s" % hugoFolder)
    else:
        LOGGER.error('Hugo command not available')