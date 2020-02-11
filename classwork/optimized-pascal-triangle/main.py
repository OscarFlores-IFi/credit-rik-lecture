import fire
import logging

from utils import timeit

logger = logging.getLogger(__name__)


class Main(object):

    def _get_element(self, i: int, j: int):
        pass

    def _naive_implementation(self, level: int, index: int = 0):
        print("Missing implementation!")

    @timeit(logger)
    def pascal_triangle(self, level: int, start: int = 0):
        self._naive_implementation(level, index=start)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    fire.Fire(Main)
