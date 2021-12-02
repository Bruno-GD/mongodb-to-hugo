import pytest
from src.mongo2hugo import generateSite

@pytest.mark.generate_site_sample
def test_generate_site():
    generateSite(['section_one', 'section_two'], {})

@pytest.mark.generate_site_db
def test_generate_site_db():
    # collect data from MongoDB
    from src.utils.db.getDataFromDB import getDataFromDB
    sections, elements = getDataFromDB()

    # generate site with collected data
    generateSite(sections, elements)