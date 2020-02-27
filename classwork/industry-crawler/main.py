import logging
import fire

from models import SIC, AbstractIndustry
from settings import *
from utils import StringWrapper, pretty_print, timeit


logger = logging.getLogger(__name__)


class Main(object):

    def _recursive_search(self, node: AbstractIndustry, string_wrapper, exact):
        title = node.title
        new_children = []
        for child in node.children:
            is_valid = self._recursive_search(node = child, string_wrapper = string_wrapper, exact = exact)
            if is_valid:
                new_children.append(child)
        successful_search = len(new_children) or string_wrapper.boolean_search(pattern = title, exact = exact, reverse = True) #len(new_children) se toma por True si tiene hijos. #reverse para revisar si el boolean se encuentra en title y no al revés.
        node.children = new_children
        return successful_search

    @staticmethod
    @timeit(logger)
    def download(filename=APP_INDUSTRY_FILE, target_url=APP_TARGET_URL):
        logging.info("Starting download procedure.")
        sic = SIC.from_url(target_url)
        sic.save(filename=filename)

    @timeit(logger)
    @pretty_print(logger)
    def search(self, title, exact=False, filename=APP_INDUSTRY_FILE):
        target_title = StringWrapper(value=title)
        sic = SIC.load(filename)
        return [
            node for node in sic.children
            if self._recursive_search(node, target_title, exact)
        ]


if __name__ == "__main__":
    logging.basicConfig(level=APP_LOG_LEVEL)
    fire.Fire(Main)
