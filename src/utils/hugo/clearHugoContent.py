from genericpath import isdir
from os import getcwd
from os.path import join
from shutil import rmtree

def clearHugoContent(hugoDir: str = join(getcwd(), 'site')) -> None:
    """
    Clear Hugo /content folder
    """

    # precondition
    assert isinstance(hugoDir, str)

    # logic
    hugoContentPath = join(hugoDir, 'content')
    if isdir(hugoDir) and isdir(hugoContentPath):
        rmtree(hugoContentPath)