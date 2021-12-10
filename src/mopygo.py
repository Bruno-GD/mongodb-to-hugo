from .utils.hugo.generateSite import generateSite
from .utils.db.getDataFromDB import getDataFromDB

def main(**kwargs) -> None:
    """
    MoPyGo main function.
    Retreive data from DB and generate site.
    """

    sections, contentOfSections = getDataFromDB(**kwargs)

    generateSite(sections, contentOfSections, **kwargs)

if __name__ == '__main__':
    from os import getenv
    from argparse import ArgumentParser

    parser = ArgumentParser(
        description="MoPyGo - Get Mongo's DB data and write Hugo content!"
    )

    # options
    parser.add_argument("-u",
        "--MONGO_URI",
        help="Set MONGO_URI to run (default from env $MONGO_URI)",
        default=getenv('MONGO_URI'),
        required=False)
    parser.add_argument("-db",
        "--MONGO_DB",
        help="Set MONGO_DB to run (default from env $MONGO_DB)",
        default=getenv('MONGO_DB'),
        required=False)
    parser.add_argument("-o",
        "--outputFolder",
        help="Set 'site' Hugo folder",
        default="site",
        required=False)
    parser.add_argument("-i"
        "--insideFolder",
        help="Set subfolder output for '/content/ Hugo folder",
        default="",
        required=False)
    args = dict(parser.parse_args()._get_kwargs())

    main(**args)