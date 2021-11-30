from os import getcwd, mkdir
from os.path import isdir, join
from shutil import rmtree

def createHugoStructure(hugoDir: str, sections: list, *, force: bool = False) -> None:
    """
    Creates a new Hugo structure at `hugoDir`
    """

    # precondition
    assert isinstance(hugoDir, str)

    # logic

    if force and isdir(hugoDir):
        rmtree(hugoDir)
        mkdir(hugoDir)
    elif not isdir(hugoDir):
        mkdir(hugoDir)

    contentDir = join(hugoDir, 'content')
    mkdir(contentDir)
    for section in sections:
        sectionDir = join(contentDir, section)

        if not isdir(sectionDir):
            mkdir(sectionDir)

        with open(join(sectionDir, 'index.md'), 'w', encoding='utf8') as file:
            file.write('')