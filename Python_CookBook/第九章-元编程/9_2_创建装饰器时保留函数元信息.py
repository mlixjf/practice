import time
from functools import wraps
from inspect import signature


def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end - start)
        return result

    return wrapper


@timethis
def countdown(n):
    """
    Counts down
    """
    while n > 0:
        n -= 1
    print("end...")


if __name__ == '__main__':
    print(countdown.__name__)
    print(countdown.__doc__)
    countdown.__wrapped__(10000)
    print(type(countdown))
    print(type(countdown.__wrapped__))
    print(dir(countdown))