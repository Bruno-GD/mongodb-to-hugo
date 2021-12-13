from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google.auth.exceptions import RefreshError

from logging import getLogger as gL
LOGGER = gL(__name__)

def checkCredentials(
    CREDENTIALS: Credentials, TOKEN_FILE: str = "token.json",
    *args, **kwargs
) -> None:
    if not CREDENTIALS.valid:
        LOGGER.warning('invalid Google credentials (invalid token or expired)')
        if CREDENTIALS.expired and CREDENTIALS.refresh_token:
            try:
                CREDENTIALS.refresh(Request())
                LOGGER.info("Refreshing token")
            except RefreshError:
                LOGGER.error("Couldn't refresh token")
            else:
                with open(TOKEN_FILE, 'w') as token:
                    token.write(CREDENTIALS.to_json())
