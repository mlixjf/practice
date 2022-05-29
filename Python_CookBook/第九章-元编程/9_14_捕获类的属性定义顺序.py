from collections import OrderedDict


class Typed:
    _expected_type = type(None)

    def __init__(self, name=None):
        self._name = name

    def __set__(self, instance, value):
        if not isinstance(value, self._expected_type):
            raise TypeError("Expected " + str(self._expected_type))
        instance.__dict__[self._name] = value


class Integer(Typed):
    _expected_type = int


class Float(Typed):
    _expected_type = float


class String(Typed):
    _expected_type = str


class OrderedMeta(type):

    def __new__(cls, clsname, bases, clsdict):
        d = dict(clsdict)
        print(d)
        order = []
        for name, value in clsdict.items():
            if isinstance(value, Typed):
                value._name = name
                order.append(name)
        d["_order"] = order
        return type.__new__(cls, clsname, bases, d)

    @classmethod
    def __prepare__(metacls, name, bases):
        return OrderedDict()


class Structure(metaclass=OrderedMeta):

    def as_csv(self):
        print(self._order)
        return ",".join(str(getattr(self, name)) for name in self._order)


class Stock(Structure):
    name = String()
    share = Integer()
    price = Float()

    def __init__(self, name, share, price):
        self.name = name
        self.share = share
        self.price = price


if __name__ == '__main__':
    stock = Stock("test", 100, 123.12)
    print(stock.as_csv())