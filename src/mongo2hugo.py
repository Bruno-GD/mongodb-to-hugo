from os import getcwd, mkdir
from os.path import join, isdir
from shutil import rmtree

from .utils.hugo.checkFolderStructure import isFolderStructure
from .utils.hugo.checkHugoCommand import isHugoAvailable
from .utils.hugo.createHugoStructure import createHugoStructure
from .utils.hugo.populateContents import populateContents
from .utils.hugo.runHugoStructure import runHugoStructure

def generateSite(sections: list, elements: dict, *, outputFolder: str = join(getcwd(), "site")) -> None:
    """
    Generate site from a list of sections and
    populate with elements inside of each section
    """

    # preconditions
    assert isinstance(sections, list)
    assert isinstance(elements, dict)
    assert isinstance(outputFolder, str)

    # logic
    if isdir(outputFolder):
        rmtree(outputFolder)
        mkdir(outputFolder)

    if isHugoAvailable():
        runHugoStructure(outputFolder)
    else:
        createHugoStructure(outputFolder)

    assert isFolderStructure(outputFolder), 'bad folder structure for Hugo'

    populateContents(outputFolder, sections, elements)


if __name__ == '__main__':
    # collect data from MongoDB
    from .utils.db.getDataFromDB import getDataFromDB
    sections, elements = getDataFromDB()

    # generate site with collected data
    generateSite(sections, elements)