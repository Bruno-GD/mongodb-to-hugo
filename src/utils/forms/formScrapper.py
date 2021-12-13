from typing import List
from .tokenRefresher import checkCredentials

from logging import getLogger as gL
LOGGER = gL(__name__)

# google spreadsheets reqs
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

def scrapSpreadsheet(
    SPREADSHEET_ID: str, RANGE: str, *args,
    TOKEN_FILE: str = "token.json", **kwargs
) -> List:
    """
    Scrap a spreadsheet from range
    """
    CREDENTIALS = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)

    checkCredentials(CREDENTIALS)

    service = build('sheets', 'v4', credentials=CREDENTIALS)
    sheet = service.spreadsheets()

    request = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE)
    response = request.execute()

    return response["values"]