from os import getcwd
from os.path import join, isdir

from .checkFolderStructure import isFolderStructure
from .createHugoStructure import createHugoStructure
from .populateContents import populateContents
from .clearHugoContent import clearHugoContent


def generateSite(
    sections: list, elements: dict, *args, insideFolder: str = "", outputFolder: str = join(getcwd(), "site"), **kwargs
) -> None:
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
        clearHugoContent(outputFolder, insideContent=insideFolder)
    else:
        createHugoStructure(outputFolder)

    populateContents(outputFolder, sections, elements, insideContent=insideFolder)

    # postcondition
    assert isFolderStructure(outputFolder)