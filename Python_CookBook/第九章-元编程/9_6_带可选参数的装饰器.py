import logging
from functools import partial, wraps


def logged(func=None, *, level=logging.DEBUG, name=None, message=None):
    if func is None:
        print("func is None")
        return partial(logged, level=level, name=name, message=message)

    log_name = name if name is not None else func.__module__
    logger = logging.getLogger(log_name)
    log_message = message if message is not None else func.__name__

    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.log(level, log_message)
        return func(*args, **kwargs)

    return wrapper


# @logged
# def add(x, y):
#     return x + y


@logged(level=logging.DEBUG, message="test")
def spam():
    print("spam")


logging.basicConfig(level=logging.DEBUG)
if __name__ == '__main__':
    # add(1, 2)
    spam()
