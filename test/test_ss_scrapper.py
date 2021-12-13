from src.utils.forms.formScrapper import scrapSpreadsheet

import pytest
from logging import getLogger as gL
LOGGER = gL(__name__)

SPREADSHEET_ID = ""
RANGE = ""

@pytest.mark.ss_scrapper
def test_scrap_ss():
    rows = scrapSpreadsheet(
        SPREADSHEET_ID,
        RANGE
    )
    LOGGER.info('spreadsheet rows: %s', rows)