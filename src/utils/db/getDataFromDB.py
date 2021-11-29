from os import getenv as getEnvironmentVariable
from typing import Tuple, Dict
from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.errors import ConnectionFailure

def getDataFromDB() -> Tuple[list, Dict[str, Collection]]:
    """
    Retreive collections and documents
    """

    MONGO_URI   = getEnvironmentVariable("MONGO_URI")
    MONGO_DB    = getEnvironmentVariable("MONGO_DB")

    assert MONGO_URI != None,   'MONGO_URI env var not set'
    assert MONGO_DB != None,    'MONGO_DB env var not set'

    try:
        CLIENT = MongoClient(MONGO_URI)         # get client instance
        DB = CLIENT.get_database(MONGO_DB)      # get db instance
        collections = DB.list_collection_names  # get all collections inside db

        collectionsData = {}
        for collection in collections:
            collectionsData[collection] = DB.get_collection(collection)
    except ConnectionFailure:
        collections = []
        collectionsData = {}
    except Exception as e:
        collections = []
        collectionsData = {}
        print('Something went wrong retreiving collections or documents:', e)
    finally:
        return collections, collectionsData
