# python native modules
from os import getenv as getEnvironmentVariable
from typing import Tuple, Dict
# pymongo imports
from pymongo import MongoClient
from pymongo.collection import Collection
# pytest logging
from logging import getLogger as gL
LOGGER = gL(__name__)
# this module imports
from .checkMongoURI import checkMongoURI

def getDataFromDB() -> Tuple[list, Dict[str, Collection]]:
    """
    Retreive collections and documents
    """

    MONGO_URI   = getEnvironmentVariable("MONGO_URI")
    MONGO_DB    = getEnvironmentVariable("MONGO_DB")

    # precondition
    assert MONGO_URI != None,   'MONGO_URI env var not set'
    assert MONGO_DB != None,    'MONGO_DB env var not set'

    checkMongoURI(MONGO_URI)

    # logic
    collections = list()
    collectionsData = dict()
    try:
        with MongoClient(MONGO_URI) as CLIENT:
            DB = CLIENT.get_database(MONGO_DB)              # get db instance
            collections = DB.list_collection_names()        # get all collections inside db

            for collection in collections:
                collectionsData[collection] = DB.get_collection(collection)
        # should close CLIENT connection
    except Exception as e:
        LOGGER.error('Something went wrong at : %s', e)
    finally:
        # postcondition
        assert isinstance(collections, list),       'collections no es lista'
        assert isinstance(collectionsData, dict),   'collectionsData no es dict'

        return collections, collectionsData
