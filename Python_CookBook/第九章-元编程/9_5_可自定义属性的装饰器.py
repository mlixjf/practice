import logging
from functools import partial, wraps


def attach_wrapper(obj, func=None):
    if func is None:
        return partial(attach_wrapper, obj)
    setattr(obj, func.__name__, func)
    return func


def logged(level, name=None, message=None):
    def decorate(func):
        log_name = name if name is not None else func.__module__
        log = logging.getLogger(log_name)
        log_message = message if message is not None else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, log_message)
            return func(*args, **kwargs)

        @attach_wrapper(wrapper)
        def set_level(new_level):
            nonlocal level
            level = new_level

        @attach_wrapper(wrapper)
        def set_message(new_message):
            nonlocal log_message
            log_message = new_message
        return wrapper

    return decorate


logging.basicConfig(level=logging.DEBUG)


@logged(logging.DEBUG)
def add(x, y):
    return x + y


if __name__ == '__main__':
    add(1, 2)
    add.set_level(logging.INFO)
    add.set_message("add test")
    add(1, 2)
