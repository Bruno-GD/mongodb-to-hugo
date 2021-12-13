from .utils.db.putDataDB import putDataIntoCollection
from .utils.forms.formScrapper import scrapSpreadsheet
from .utils.hugo.generateSite import generateSite
from .utils.db.getDataFromDB import getDataFromDB
from .utils.forms.ssClear import clearSpreadsheet

def main(**kwargs) -> None:
    """
    MoPyGo main function.
    Retreive data from DB and generate site.
    """

    ssRows = scrapSpreadsheet(**kwargs)
    if len(ssRows) > 1:
        keys = ssRows[0][2:]

        restaurants = {}
        for row in ssRows[1:]:
            restaurant = dict(zip(keys, row[2:]))
            restaurant["price"] = int(restaurant["price"])
            restaurant["capacity"] = int(restaurant["capacity"])
            restaurant["menu"] = []
            restaurantType = row[0]

            if not restaurantType in restaurants:
                restaurants[restaurantType] = []
            restaurants[restaurantType].append(restaurant)

        for restType in restaurants:
            putDataIntoCollection(restType, restaurants[restType], **kwargs)

    clearSpreadsheet(**kwargs)

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
    parser.add_argument("-t",
        "--TOKEN_FILE",
        help="set token.json file path",
        default="token.json",
        required=False
    )
    parser.add_argument("-ss",
        "--SPREADSHEET_ID",
        help="Set spreadsheet id to get new data",
        required=True,
        type=str
    )
    parser.add_argument("-r",
        "--RANGE",
        help="Set range of spreadsheet",
        required=True,
        type=str
    )
    parser.add_argument("-cr"
        "--CLEAR_RANGE",
        help="Set range to clear data from spreadsheet",
        required=True,
        type=str
    )
    args = dict(parser.parse_args()._get_kwargs())

    main(**args)