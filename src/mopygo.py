from .utils.hugo.generateSite import generateSite
from .utils.db.getDataFromDB import getDataFromDB

def main(*args):
    """
    MoPyGo main function.
    Retreive data from DB and generate site.
    """

    sections, contentOfSections = getDataFromDB()

    generateSite(sections, contentOfSections)

if __name__ == '__main__':
    main()