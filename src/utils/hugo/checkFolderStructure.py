# pytest
from logging import getLogger as gL

LOGGER = gL(__name__)
# python native
from os.path import isdir as dirExists, join
from os import getcwd

HUGO_STRUCTURE = ["archetypes", "content", "data", "static", "themes"]


def isFolderStructure(hugoContent: str) -> bool:
    """
    check if Hugo structure is correct
    """

    # precondition
    assert isinstance(hugoContent, str)

    # logic
    for path in HUGO_STRUCTURE:
        fullpath = join(hugoContent, path)
        if not dirExists(fullpath):
            LOGGER.info(fullpath)
            return False

    return True
