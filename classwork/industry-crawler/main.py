import logging
import fire

from models import SIC
from settings import *
from utils import StringWrapper, pretty_print, timeit


logger = logging.getLogger(__name__)


class Main(object):

    def _recursive_search(self, node, string_wrapper, exact):
        pass

    @staticmethod
    @timeit(logger)
    def download(filename=APP_INDUSTRY_FILE, target_url=APP_TARGET_URL):
        logging.info("Starting download procedure.")
        sic = SIC.from_url(target_url)
        sic.save(filename=filename)

    @timeit(logger)
    @pretty_print(logger)
    def search(self, title, exact=False, filename=APP_INDUSTRY_FILE):
        pass


if __name__ == "__main__":
    logging.basicConfig(level=APP_LOG_LEVEL)
    fire.Fire(Main)
