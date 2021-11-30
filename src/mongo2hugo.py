from os.path import join
from os import getcwd

from .utils.hugo.checkHugoCommand       import isHugoAvailable
from .utils.hugo.createHugoStructure    import createHugoStructure
from .utils.hugo.checkFolderStructure   import isFolderStructure
from .utils.hugo.runHugoStructure       import runHugoStructure

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
    if not isFolderStructure(outputFolder):
        if isHugoAvailable():
            runHugoStructure(outputFolder)
        else:
            createHugoStructure(outputFolder, sections)


if __name__ == '__main__':
    # collect data from MongoDB
    from .utils.db.getDataFromDB import getDataFromDB
    sections, elements = getDataFromDB()

    # generate site with collected data
    generateSite(sections, elements)