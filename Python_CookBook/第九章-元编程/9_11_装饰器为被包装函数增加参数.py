import inspect
from functools import wraps


def optional_debug(func):
    @wraps(func)
    def wrapper(*args, debug=False, **kwargs):
        if debug:
            print("calling", func.__name__)
        return func(*args, **kwargs)

    return wrapper


@optional_debug
def add(x, y):
    return x + y


def optional_debug2(func):
    if "debug" in inspect.signature(func).parameters:
        raise TypeError("debug argument already defined")

    @wraps(func)
    def wrapper(*args, debug=False, **kwargs):
        if debug:
            print("Calling", func.__name__)
        return func(*args, **kwargs)

    return wrapper


@optional_debug2
def a(x, y):
    pass


@optional_debug2
def b(x, y):
    pass


@optional_debug2
def c(x, y, z):
    pass


def test(x, y):
    pass


def optional_debug3(func):
    if "debug" in inspect.signature(func).parameters:
        raise TypeError("debug argument already defined")

    @wraps(func)
    def wrapper(*args, debug=False, **kwargs):
        if debug:
            print("Calling", func.__name__)
        return func(*args, **kwargs)

    sig = inspect.signature(func)
    params = list(sig.parameters.values())
    params.append(inspect.Parameter("debug", inspect.Parameter.KEYWORD_ONLY, default=False))
    wrapper.__signature = sig.replace(parameters=params)
    return wrapper


@optional_debug3
def test(x, y):
    pass


if __name__ == '__main__':
    add(1, 2)
    add(1, 2, debug=True)
    print(inspect.signature(c))

    print(c.__dict__)
    print(dir(c))
    print(c.__code__)

    print(inspect.signature(test).parameters)