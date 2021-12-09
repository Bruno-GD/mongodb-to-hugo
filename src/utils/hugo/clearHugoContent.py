from genericpath import isdir
from os import getcwd, mkdir
from os.path import join
from shutil import rmtree

# pytest
from logging import getLogger as gL

LOGGER = gL(__name__)


def clearHugoContent(hugoDir: str = join(getcwd(), "site")) -> None:
    """
    Clear Hugo /content folder
    """

    # precondition
    assert isinstance(hugoDir, str)

    # logic
    hugoContentPath = join(hugoDir, "content")
    if isdir(hugoDir) and isdir(hugoContentPath):
        rmtree(hugoContentPath)
        LOGGER.info("removed %s", hugoContentPath)

    if not isdir(hugoContentPath):
        mkdir(hugoContentPath)
        LOGGER.info("mkdir %s", hugoContentPath)
