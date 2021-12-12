from pymongo import MongoClient
from pymongo.errors import InvalidName

from os import getenv

from logging import getLogger as gL

LOGGER = gL(__name__)

def putDataIntoCollection(
    COLLECTION_NAME: str, DOCUMENTS: list[dict], *, COLLECTION_DESCRIPTION: str = "",
    MONGO_URI: str = getenv('MONGO_URI'), MONGO_DB: str = getenv('MONGO_DB')
) -> None:
    """
    Insert into MongoDB
    """

    try:
        with MongoClient(MONGO_URI) as CLIENT:
            DB = CLIENT.get_database(MONGO_DB)
            TYPES_COLLECTION = DB.get_collection('types')

            if TYPES_COLLECTION.count_documents({"name": COLLECTION_NAME}) == 0:
                TYPES_COLLECTION.insert_one({
                    "name": COLLECTION_NAME,
                    "description": COLLECTION_DESCRIPTION
                })

            try:
                newCollection = DB.get_collection(COLLECTION_NAME)
            except InvalidName:
                newCollection = DB.create_collection(COLLECTION_NAME)
            finally:
                newCollection.insert_many(DOCUMENTS)
    except InvalidName:
        LOGGER.warn('invalid name')
    except Exception as e:
        LOGGER.error('error %s', e)