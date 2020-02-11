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
