import math
import time

from math import sqrt
from timeit import timeit


def compute_roots_1(numbers):
    result = []
    for n in numbers:
        result.append(math.sqrt(n))


def compute_roots_2(numbers):
    result = []
    appender = result.append
    for n in numbers:
        appender(sqrt(n))


def compute_roots_3(numbers):
    result = []
    new_sqrt = math.sqrt
    appender = result.append
    for n in numbers:
        appender(new_sqrt(n))


nums = range(1000000)


def run(func, number):
    start = time.time()
    for n in range(number):
        func(nums)
    stop = time.time()
    print(func.__name__, ":", stop - start)


print("compute_roots_1:", timeit("compute_roots_1(nums)", "from __main__ import compute_roots_1, nums", number=100))
print("compute_roots_2:", timeit("compute_roots_2(nums)", "from __main__ import compute_roots_2, nums", number=100))
print("compute_roots_3:", timeit("compute_roots_3(nums)", "from __main__ import compute_roots_3, nums", number=100))


class A:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value



a = A(1, 2)
print(timeit("a.x", "from __main__ import a"))
print(timeit("a.y", "from __main__ import a"))