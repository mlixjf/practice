class Structure1(object):
    _fields = []

    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise TypeError("Expected {} arguments".format(len(self._fields)))

        for name, value in zip(self._fields, args):
            setattr(self, name, value)


class Stock(Structure1):
    _fields = ["name", "shares", "price"]


class Point(Structure1):
    _fields = ["x", "y"]


class Structure2(object):
    _fields = []

    def __init__(self, *args, **kwargs):
        if len(args) > len(self._fields):
            raise TypeError("Expected {} arguments".format(len(self._fields)))

        for name, value in zip(self._fields, args):
            setattr(self, name, value)

        for name in self._fields[len(args):]:
            setattr(self, name, kwargs[name])


class Stock2(Structure2):
    _fields = ["name", "shares", "price"]


class Structure3(object):
    _fields = []

    def __init__(self, *args, **kwargs):
        if len(args) != len(self._fields):
            raise TypeError("Expected {} arguments".format(self._fields))

        for name, value in zip(self._fields, args):
            setattr(self, name, value)

        extra_args = kwargs.keys() - self._fields
        for arg in extra_args:
            setattr(self, arg, kwargs[arg])


class Stock3(Structure3):
    _fields = ["name", "shares", "price"]


if __name__ == '__main__':
    stock = Stock("ACME", 50, 9.1)
    print(stock.__dict__)
    print(Stock.__dict__)

    point = Point(1, 1)
    print(point.__dict__)
    print(Point.__dict__)

    s = Stock2("ACME", 50, price=9.2)
    print(s.__dict__)

    st = Stock3("ACME", 50, 9.2, date="2022-04-23")
    print(st.__dict__)