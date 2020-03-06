import logging
import fire
import os

from utils import pretty_print
from utils import flatten_dict
from models import load

logger = logging.getLogger(__name__)

class Main(object):

    @staticmethod
    @pretty_print(logger)
    def show(filename):
        return load(filename)

    @staticmethod
    @pretty_print(logger)
    def flatten(filename):
        return flatten_dict(load(filename))

if __name__ == "__main__":
    logging.basicConfig(level=os.environ.get("APP_LOG_LEVEL",default="INFO"))
    fire.Fire(Main)

