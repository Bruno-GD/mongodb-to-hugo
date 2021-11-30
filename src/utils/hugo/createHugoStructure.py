from os import getcwd, mkdir
from os.path import join
from .checkFolderStructure import HUGO_STRUCTURE

def createHugoStructure(hugoDir: str = join(getcwd(), 'site')) -> None:
    """
    Creates a new Hugo structure at `hugoDir`
    """

    # precondition
    assert isinstance(hugoDir, str)

    # logic
    for path in HUGO_STRUCTURE:
        fullpath = join(hugoDir, path)
        mkdir(fullpath)