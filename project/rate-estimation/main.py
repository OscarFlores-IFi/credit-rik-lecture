import fire
import logging

from settings import EXPECTED_RATE_LOG_LEVEL
from models.drive import (
    ConfigTable,
    RateValue,
    RequestValue,
    ResultTable
)
from models.finance import Amortization
from utils import setup

import pandas as pd

logger = logging.getLogger(__name__)


class Main:

    @staticmethod
    def setup():
        setup()


if __name__ == "__main__":
    logging.basicConfig(level=EXPECTED_RATE_LOG_LEVEL)
    pd.options.display.float_format = '{:,.2f}'.format
    fire.Fire(Main)
