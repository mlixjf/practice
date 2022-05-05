from functools import wraps


def somedecorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("somedecorator")
        return func(*args, **kwargs)

    return wrapper


@somedecorator
def add(x, y):
    return x + y


if __name__ == '__main__':
    orig_add = add.__wrapped__
    print(orig_add(1, 2))
