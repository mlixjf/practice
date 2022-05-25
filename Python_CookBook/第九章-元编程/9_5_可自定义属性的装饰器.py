import logging
import time
from functools import partial, wraps


def timethis(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        stop = time.time()
        print(func.__name__, ":", stop - start)
        return result
    return wrapper


def attach_wrapper(obj, func=None):
    if func is None:
        return partial(attach_wrapper, obj)
    setattr(obj, func.__name__, func)
    return func


def logged(level, name=None, message=None):
    def decorate(func):
        log_name = name if name is not None else func.__name__
        logger = logging.getLogger(log_name)
        log_message = message if message is not None else func.__module__

        @wraps(func)
        def wrapper(*args, **kwargs):
            logger.log(level, log_message)
            return func(*args, **kwargs)

        @attach_wrapper(wrapper)
        def set_level(new_level):
            nonlocal level
            level = new_level

        @attach_wrapper(wrapper)
        def set_msg(new_message):
            nonlocal log_message
            log_message = new_message

        return wrapper

    return decorate


@timethis
@logged(logging.DEBUG)
def add(x, y):
    return x + y


logging.basicConfig(level=logging.DEBUG)

if __name__ == '__main__':
    add.set_msg('dsfdasfdsa')
    add.set_level(logging.INFO)
    print(add(1, 2))

