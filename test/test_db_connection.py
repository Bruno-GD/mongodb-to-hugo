import pytest
from src.utils.db.getDataFromDB import getDataFromDB

@pytest.mark.db_connection
def test_db_connection():
    collectionNames, collections = getDataFromDB()
    assert isinstance(collectionNames, list), 'collectionNames no es una lista'
    assert isinstance(collections, dict), 'collections no es un diccionario'