import fire
import logging
from utils import pretty_print
from utils import sum_levels as sl
from models import Node


logger = logging.getLogger(__name__)


class Main(object):

    @pretty_print(logger)
    def show(self, filename):
        return Node.load(filename)

    @staticmethod
    @pretty_print(logger)
    def sum_levels(filename):
        return sl(Node.load(filename))



if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    fire.Fire(Main)


filename = "ex-1.json"
tmp = Node.load(filename)
