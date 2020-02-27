import os


APP_PROJECT_DIRECTORY = os.environ.get(
    "APP_PROJECT_DIRECTORY",
    default=os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
)

APP_LOG_LEVEL = os.environ.get(
    "APP_LOG_LEVEL",
    default="INFO"
)

APP_TARGET_URL = os.environ.get(
    "APP_TARGET_URL",
    default="https://www.osha.gov/pls/imis/sic_manual.html"
)

APP_INDUSTRY_FILE = os.environ.get(
    "APP_INDUSTRY_FILE",
    default="industries.json"
)
