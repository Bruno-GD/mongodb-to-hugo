import pytest
from src.mongo2hugo import generateSite

@pytest.mark.generate_site
def test_generate_site():
    generateSite(['section_one', 'section_two'], {})