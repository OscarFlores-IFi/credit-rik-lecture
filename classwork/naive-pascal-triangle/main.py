import fire
import logging

from utils import timeit

logger = logging.getLogger(_name_)


class Main(object):

    def _get_element(self, i: int, j: int):
        return 1 if (j == 0 or j>=i) else \
            self._get_element(i=i-1, j=j) + self._get_element(i = i-1, j = j-1)

    def _naive_implementation(self, level: int, index: int = 0):
        if index < level:
            row = [str(self._get_element(i = index, j = j)) for j in range(index+1)]
            print(" ".join(row))
            self._naive_implementation(level = level, index = index + 1)


    @timeit(logger)
    def pascal_triangle(self, level: int, start: int = 0):
        self._naive_implementation(level, index=start)


if _name_ == "_main_":
    logging.basicConfig(level=logging.INFO)
    fire.Fire(Main)