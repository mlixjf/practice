import math
from typing import Union


class lazyproperty:

    def __init__(self, func):
        self.func = func

    def __get__(self, instance, cls):
        if instance is None:
            return None
        else:
            value = self.func(instance)
            setattr(instance, self.func.__name__, value)
            return value


class Circle(object):

    def __init__(self, radius: Union[int, float]) -> None:
        self.radius = radius

    @lazyproperty
    def area(self) -> float:
        print("Computing area")
        return math.pi * self.radius ** 2

    @lazyproperty
    def perimeter(self) -> float:
        print("Computing perimeter")
        return 2 * math.pi * self.radius


if __name__ == '__main__':
    c = Circle(2)
    print(c.area)
    print(c.area)
