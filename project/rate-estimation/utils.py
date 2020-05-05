import os
import logging
import pickle
import string
from typing import Callable, List, Optional

import jax.numpy as np
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


from settings import (
    EXPECTED_RATE_GOOGLE_SHEET_SERVICE_NAME,
    EXPECTED_RATE_GOOGLE_SHEET_SERVICE_VERSION,
    EXPECTED_RATE_CREDENTIALS_FILE,
    EXPECTED_RATE_CACHE_CREDENTIALS_FILE,
    EXPECTED_RATE_SCOPES
)

logger = logging.getLogger(__name__)


def get_creds_from_cache() -> Optional[Credentials]:
    logger.info("Getting creds from cache file: %s", EXPECTED_RATE_CACHE_CREDENTIALS_FILE)
    creds = None
    if os.path.exists(EXPECTED_RATE_CACHE_CREDENTIALS_FILE):
        with open(EXPECTED_RATE_CACHE_CREDENTIALS_FILE, "rb") as token:
            creds = pickle.load(token)
    else:
        logger.warning("Credentials not found on cache file.")
    return creds


def cache_creds(creds: Credentials) -> Credentials:
    logger.info("Saving creds into cache file: %s", EXPECTED_RATE_CACHE_CREDENTIALS_FILE)
    with open(EXPECTED_RATE_CACHE_CREDENTIALS_FILE, "wb") as token:
        pickle.dump(creds, token)
    return creds


def setup() -> Credentials:
    logger.info("Running the setup() function.")
    # Get credentials from cache file.
    creds = get_creds_from_cache()
    if creds is None:
        logger.info("Running the installment flow.")
        # Get credentials from flow if cache does not exists.
        flow = InstalledAppFlow.from_client_secrets_file(
            client_secrets_file=EXPECTED_RATE_CREDENTIALS_FILE,
            scopes=EXPECTED_RATE_SCOPES
        )
        creds = flow.run_local_server(port=0)
    elif creds.expired and creds.refresh_token:
        logger.info("Running the refresh flow.")
        # Refresh creds if needed.
        creds.refresh(Request())
    return cache_creds(creds)


def get_google_sheet_service():
    credentials = setup()
    service = build(
        serviceName=EXPECTED_RATE_GOOGLE_SHEET_SERVICE_NAME,
        version=EXPECTED_RATE_GOOGLE_SHEET_SERVICE_VERSION,
        credentials=credentials,
        cache_discovery=False,
    )
    return service.spreadsheets()


def get_spreadsheet_column_names(column_index_max: int, ref_cols: Optional[List[str]] = None):
    if ref_cols is None:
        ref_cols = [c for c in string.ascii_uppercase]
    condition = int(column_index_max / len(ref_cols))
    if not condition:
        return ref_cols[:column_index_max]
    cols = ref_cols + [col + new_col for col in ref_cols for new_col in string.ascii_uppercase]
    return get_spreadsheet_column_names(column_index_max, ref_cols=cols)
