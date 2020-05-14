import os
import logging


EXPECTED_RATE_LOG_LEVEL = os.environ.get(
    "EXPECTED_RATE_LOG_LEVEL",
    default=logging.INFO
)

EXPECTED_RATE_CREDENTIALS_FILE = os.environ.get(
    "EXPECTED_RATE_CREDENTIALS_FILE",
    default="credentials.json"
)

EXPECTED_RATE_CACHE_CREDENTIALS_FILE = os.environ.get(
    "EXPECTED_RATE_CACHE_CREDENTIALS",
    default="token.pickle"
)

EXPECTED_RATE_SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets"
]

EXPECTED_RATE_GOOGLE_SHEET_SERVICE_NAME = "sheets"

EXPECTED_RATE_GOOGLE_SHEET_SERVICE_VERSION = "v4"
