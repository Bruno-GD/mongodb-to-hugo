from typing import List

from logging import getLogger as gL
LOGGER = gL(__name__)

# google spreadsheets reqs
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from google.auth.exceptions import RefreshError
from google.oauth2.credentials import Credentials

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

def scrapSpreadsheet(
    SPREADSHEET_ID: str, RANGE: str = "Items!A:Z", *,
    CREDS: dict = {},
) -> List:
    """
    Scrap a spreadsheet from range
    """
    CREDENTIALS = Credentials.from_authorized_user_file('token.json', SCOPES)

    if not CREDENTIALS.valid:
        LOGGER.warning('invalid Google credentials (invalid token or expired)')
        if CREDENTIALS.expired and CREDENTIALS.refresh_token:
            try:
                CREDENTIALS.refresh(Request())
                LOGGER.info("Refreshing token")
            except RefreshError:
                LOGGER.error("Couldn't refresh token")
            else:
                with open('token.json', 'w') as token:
                    token.write(CREDENTIALS.to_json())
        

    service = build('sheets', 'v4', credentials=CREDENTIALS)
    sheet = service.spreadsheets()

    request = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE)
    response = request.execute()

    return response["values"]