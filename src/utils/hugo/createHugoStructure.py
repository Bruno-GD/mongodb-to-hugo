from os import getcwd, mkdir
from os.path import join

from .checkHugoCommand import isHugoAvailable
from .hugoCommands import startHugoSite
from .checkFolderStructure import HUGO_STRUCTURE, isFolderStructure

def createHugoStructure(hugoDir: str = join(getcwd(), 'site')) -> None:
    """
    Creates a new Hugo structure at `hugoDir`
    """

    # precondition
    assert isinstance(hugoDir, str)

    # logic
    if isHugoAvailable():
        startHugoSite(hugoDir)
    else:
        for path in HUGO_STRUCTURE:
            fullpath = join(hugoDir, path)
            mkdir(fullpath)

    # postcondition
    assert isFolderStructure(hugoDir)