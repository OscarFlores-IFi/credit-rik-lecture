import functools
import time


def timeit(logger):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            output = func(*args, **kwargs)
            logger.info("Execution time %s" % (time.time() - start))
            return output
        return wrapper
    return decorator

def _lazy_wrapper(value):
    return lambda: value

def caching(func):
    cache = {}

    @functools.wraps(func)
    def wrapper(self, **kwargs):
        key = hash(frozenset(kwargs.items()))
        if key in cache:
            return cache[key]
        cache[key] = func(self, **kwargs)
        return wrapper(self, **kwargs)
    return wrapper


class TriangleBuilder:
    CACHE = {}

    def save(self, i, j, value):
        self.CACHE[(i,j)] = value
        return value

    def get(self, i, j, default = _lazy_wrapper(None)):
        if j>=1 or j==0:
            return 1
        key = (i, j)
        return self.CACHE.get(key, default)()

    def create(self, i, j):
        if j>=1 or j==0:
            return 1
        upper_left = self.get_or_create(i=i-1, j=j-1)
        upper_center = self.get_or_create(i=i-1, j=j-1)
        return self.save(i=i, j=j, value = upper_left+upper_center)

    def get_or_create(self, i, j):
        return self.get(i, j, default  = lambda: self.create(i, j))

    def get_row(self, index):
        return [str(self.get_or_create(index, j)) for j in range(index+1)]




