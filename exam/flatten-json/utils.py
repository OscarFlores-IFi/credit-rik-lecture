import functools
import json
import logging


def pretty_print(logger, serializer_function=lambda obj: obj.__dict__):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            serializable_obj = func(*args, **kwargs)
            try:
                formatted_output = json.dumps(serializable_obj, indent=4, default=serializer_function)
                print(formatted_output)
            except TypeError as e:
                logger.error("Type Error encounter with message {error}".format(error=e))
                raise  # Re-throw exception to fail the program execution with stack-trace.
        return wrapper
    return decorator



@pretty_print(logging.getLogger(__name__))
def flatten_dict(dict):
    res = {}

    def flatten(x, name=''):
        if isinstance(x, dict):
            for i in x.keys():
                flatten(x[i], name + i + '.')
        elif isinstance(x, list):
            for i in range(len(x)):
                flatten(x[i], name + str(i) + '.')
        else:
            res[name[:-1]] = x

    flatten(dict)
    return res