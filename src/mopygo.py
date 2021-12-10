from .utils.hugo.generateSite import generateSite
from .utils.db.getDataFromDB import getDataFromDB

def main(*args, **kwargs) -> None:
    """
    MoPyGo main function.
    Retreive data from DB and generate site.
    """

    sections, contentOfSections = getDataFromDB(*args)

    generateSite(sections, contentOfSections, **kwargs)

if __name__ == '__main__':
    insideContentFolder = input('Nombre de carpeta de contenido? .../content/')
    main(insideFolder=insideContentFolder)