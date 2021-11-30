# pytest
from logging import getLogger as gL
LOGGER = gL(__name__)
# python native
from os.path import isdir as dirExists, isfile as fileExists, join
from os import getcwd
# this module
from .createHugoStructure import createHugoStructure

HUGO_STRUCTURE = [
    'archetypes',
    'content',
    'data',
    'layouts',
    'static',
    'themes',
    'config.toml'
]

def isFolderStructure(hugoContent: str) -> bool:
    """
    check if hugoContent folder exists
    """

    # precondition
    assert isinstance(hugoContent, str)

    # logic
    for path in HUGO_STRUCTURE:
        fullpath = join(getcwd(), hugoContent, path)
        if not dirExists(fullpath) and not fileExists(fullpath):
            return False

    return True