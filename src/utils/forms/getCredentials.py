from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

from .formScrapper import SCOPES

def getNewCredentials():
    """
    Log in to get new credentials
    """
    flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
    creds = flow.run_local_server(port=0)

    with open('token.json', 'w') as token:
        token.write(creds.to_json())