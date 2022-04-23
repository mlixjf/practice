class Integer(object):

    def __init__(self, name: str) -> None:
        self.name = name

    def __get__(self, instance, cls):
        if instance is None:
            return None
        else:
            return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError("Expected an int")

        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]


class Point(object):
    x = Integer("x")
    y = Integer("y")

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y


class Point1(object):

    def __init__(self, x, y):
        self.x = Integer("x")
        self.y = Integer("y")


class Typed(object):

    def __init__(self, name: str, expected_type: type):
        self.name = name
        self.expected_type = expected_type

    def __get__(self, instance, cls):
        if instance is None:
            return None
        else:
            return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError("Expected an {}".format(self.expected_type.__name__))
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]


def type_assert(**kwargs):
    def decorate(cls):
        for name, expected_type in kwargs.items():
            setattr(cls, name, Typed(name, expected_type))
            return cls

    return decorate


# @type_assert(name=str, shares=int, price=float)
class Stock(object):

    def __init__(self, name: str, shares: int, price: float):
        self.name = name
        self.shares = shares
        self.price = price


if __name__ == '__main__':
    p = Point(1, 1)
    print(p.x)

    p1 = Point1(1, 1)
    print(p1.x)

    s = Stock("test", 100, 100.1)
    print(s.name)
    # s.name = 1

    temp = type_assert(name=str, shares=int, price=float)

    S = temp(Stock)
    s2 = S("test", 100, 100.1)
    print(s2.name)