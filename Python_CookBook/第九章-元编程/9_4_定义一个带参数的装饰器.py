import logging
from functools import wraps

logging.basicConfig(level=logging.DEBUG)


def logged(level, name=None, message=None):
    def decorate(func):
        log_name = name if name is not None else func.__module__
        log = logging.getLogger(log_name)
        log_message = message if message is not None else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, log_message)
            return func(*args, **kwargs)
        return wrapper
    return decorate


@logged(logging.INFO)  # x = logged(logging.INFO)(func)
def add(x: int, y: int) -> int:
    return x + y


if __name__ == '__main__':
    print(add(1, 2))
