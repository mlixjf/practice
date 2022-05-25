import logging
import sys
from functools import partial


class C:
    x = 1

    def __init__(self, y):
        self.y = y

    def fun(self):
        print(self.y)


def add(x, y):
    return x + y


class Test:
    tt = 1

    def tt(self):
        print("tt")


if __name__ == '__main__':
    c = C(2)
    print(c.__dict__)
    print(vars(c))

    print(C.__dict__)
    print(type(c).__dict__)

    c.fun()
    print(c.__dict__["y"])
    # type(c).__dict__["fun"]()

    t = Test()
    print(t, file=sys.stderr)
    print()

    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger("test")
    logger.log(level=logging.DEBUG, msg="213213")

    new = partial(add, x=1)
    # new(2)
    add(1, x=2)