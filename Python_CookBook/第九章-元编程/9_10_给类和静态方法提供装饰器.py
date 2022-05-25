import time
from abc import ABCMeta, abstractmethod
from functools import wraps


def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        r = func(*args, **kwargs)
        stop = time.time()
        print("func:{}, cost:{}".format(func.__name__, stop - start))
        return r

    return wrapper


class Spam:

    @timethis
    def instance_method(self, n):
        print(self, n)
        while n > 0:
            n -= 1

    @classmethod
    @timethis
    def class_method(cls, n):
        print(cls, n)
        while n > 0:
            n -= 1

    @staticmethod
    @timethis
    def static_method(n):
        print(n)
        while n > 0:
            n -= 1


class A(metaclass=ABCMeta):

    @classmethod
    @abstractmethod
    def method(cls):
        pass


class B(A):

    @classmethod
    def method(cls):
        pass


if __name__ == '__main__':
    s = Spam()
    s.instance_method(10)
    s.class_method(10)
    s.static_method(10)

    b = B()