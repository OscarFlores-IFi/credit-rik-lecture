import fire
import logging

from utils import timeit

logger = logging.getLogger(__name__)


class Main(object):

    def _get_element(self, i: int, j: int):
        return 1 if (j == 0 or j>=i) else \
            self._get_element(i=i-1, j=j) + self._get_element(i = i-1, j = j-1)

    def _naive_implementation(self, level: int, index: int = 0):
        if index < level:
            row = [str(self._get_element(i = index, j = j)) for j in range(index+1)]
            print(" ".join(row))
            self._naive_implementation(level = level, index = index + 1)

    def _optimized_implementation(self, level: int, index : int = 0):
        if index<level:
            row = [str(self._get_element(i=index,j=j)) for j in range(index+1)]
            print(" ".join(row))
            self._optimized_implementation(level=level, index=index+1)


    @timeit(logger)
    def pascal_triangle(self, level: int, option: str, start: int = 0):
        if "naive" == option.lower():
            self._naive_implementation(level, index=start)
        if "optimized" == option.lower():
            self._optimized_implementation(level, index=start)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    fire.Fire(Main)