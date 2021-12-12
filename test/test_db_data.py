import pytest

from json import load
from os.path import join
from os import getcwd
from random import choice, choices, randint

from src.utils.db.putDataDB import putDataIntoCollection

MONGO_URI=""
MONGO_DB=""

from logging import getLogger as gL
LOGGER = gL(__name__)

@pytest.mark.put_data_db
def test_put_data():
    putDataIntoCollection(
        "chinese",
        [
            {
                "name":"Johuan Las",
                "location":"Wall Street",
                "price":305,
                "menu":[
                    {
                        "menuName":"Del suelo al plato",
                        "first":"Arroz 3 delicias",
                        "second":"Sopica",
                        "desert":"Chocolate"
                    },
                    {
                        "menuName":"De la calle a tu casa",
                        "first":"Arroz 3 delicias",
                        "second":"Sopica",
                        "desert":"Chocolate"
                    }
                ],
                "capacity":5,
                "image":"asiaticoArroz.jpeg"
            }
        ],
    MONGO_URI=MONGO_URI, MONGO_DB=MONGO_DB)

@pytest.mark.populate_content
def test_populate_content():
    MOCKS = join(getcwd(), 'mocks')
    IMGS = {
        "chinese": ['asiaticoArroz.jpeg', 'asiaticoFideos.jpeg', 'asiaticoSushi.jpeg'],
        "american": ['americanoHotDog.jpeg', 'americanoHamburguesa2.jpeg', 'americanoPollo.jpeg'],
        "italian": ['italianoEsalada.jpeg', 'italianoPasta.jpeg', 'italianoPizza.jpeg']
    }
    menuList = load(open(join(MOCKS, 'menus.json'), 'r', encoding='utf8'))

    RESTS = {
        "chinese": load(open(join(MOCKS, 'restaurants_chinese.json'), 'r')),
        "american": load(open(join(MOCKS, 'restaurants_american.json'), 'r')),
        "italian": load(open(join(MOCKS, 'restaurants_italian.json'), 'r'))
    }

    for restName in RESTS:
        rests = RESTS[restName]
        docs = []
        for restData in rests:
            docs.append({
                "name": restData['name'],
                "location":restData['address']['street'],
                "price": randint(1, 1000),
                "menu": choices(menuList, k=randint(1, 8)),
                "capacity": randint(2, 20),
                "image": choice(IMGS[restName])
            })

        putDataIntoCollection(
        restName,
        docs,
        MONGO_URI=MONGO_URI, MONGO_DB=MONGO_DB)
