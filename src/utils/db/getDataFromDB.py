# python native modules
from os import getenv as getEnvironmentVariable

# pymongo imports
from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.errors import InvalidName

# pytest logging
from logging import getLogger as gL

LOGGER = gL(__name__)
# this module imports
from .checkMongoURI import checkMongoURI


def getDataFromDB(
    MONGO_URI: str = getEnvironmentVariable("MONGO_URI"), MONGO_DB: str = getEnvironmentVariable("MONGO_DB"), *args, **kwargs
) -> tuple[list[dict], dict[str, list]]:
    """
    Retreive collections and documents
    """

    # precondition
    assert MONGO_URI != None, "MONGO_URI env var not set"
    assert MONGO_DB != None, "MONGO_DB env var not set"

    checkMongoURI(MONGO_URI)  # warn srv usage

    # logic
    collectionNames = list()
    collections = dict()
    try:
        with MongoClient(MONGO_URI) as CLIENT:
            DB = CLIENT.get_database(MONGO_DB)  # get db instance
            TYPES_COLLECTION = DB.get_collection('types') # get collection instance of 'types'
            collectionNames = list(TYPES_COLLECTION.find({}))

            for collectionName in collectionNames:
                try:
                    collection = DB.get_collection(collectionName)
                except InvalidName:
                    LOGGER.warn("The collection %s doesn't exist and it's on 'types' collection", collectionName)
                except Exception as error:
                    LOGGER.warn("Error getting collection %s", error.with_traceback())
                else:
                    collections[collectionName] = list(collection.find({}))
        # should close CLIENT connection
    except Exception as e:
        LOGGER.error("Something went wrong at : %s", e)
    finally:
        # postcondition
        assert isinstance(collectionNames, list), "collections no es lista"
        assert isinstance(collections, dict), "collectionsData no es dict"

        return collectionNames, collections
