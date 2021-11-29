from os.path import join
from os import getcwd

from src.utils.hugo.createHugoStructure import createHugoStructure

from .utils.hugo.checkFolderStructure import isFolderStructure

def generateSite(sections: list, elements: dict, *, outputFolder: str = join(getcwd(), "content")) -> None:
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
        createHugoStructure(outputFolder, sections)


if __name__ == '__main__':
    # collect data from MongoDB
    from .utils.db.getDataFromDB import getDataFromDB
    sections, elements = getDataFromDB()

    # generate site with collected data
    generateSite(sections, elements)