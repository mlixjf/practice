class Descriptor:

    def __init__(self, name=None, **opts):
        self.name = name
        for key, value in opts.items():
            setattr(self, key, value)

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value


class Typed(Descriptor):
    expected_type = type(None)

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError("Expected %s" % str(self.expected_type))
        super().__set__(instance, value)


class Unsigned(Descriptor):

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Expected >= 0")
        super().__set__(instance, value)


class MaxSized(Descriptor):

    def __init__(self, name=None, **opts):
        if "size" not in opts:
            raise TypeError("missing size option")
        super().__init__(name, **opts)

    def __set__(self, instance, value):
        if len(value) >= self.size:
            raise ValueError("size must be <" + str(self.size))
        super().__set__(instance, value)


class Integer(Typed):
    expected_type = int


class UnsignedInteger(Integer, Unsigned):
    pass


class Float(Typed):
    expected_type = float


class UnsignedFloat(Float, Unsigned):
    pass


class String(Typed):
    expected_type = str


class SizedString(String, MaxSized):
    pass


class Stock:
    name = SizedString("name", size=8)
    shares = UnsignedInteger("shares")
    price = UnsignedFloat("price")

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price


def check_attributes(**kwargs):
    def decorate(cls):
        for key, value in kwargs.items():
            if isinstance(value, Descriptor):
                value.name = key
                setattr(cls, key, value)
            else:
                setattr(cls, key, value(key))
        return cls

    return decorate


@check_attributes(name=SizedString(size=8), shares=UnsignedInteger, price=UnsignedFloat)
class Stock1:

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price


class CheckMeta(type):

    def __new__(cls, clsname, bases, methods):
        for key, value in methods.items():
            if isinstance(value, Descriptor):
                value.name = key
        return type.__new__(cls, clsname, bases, methods)


class Stock3(metaclass=CheckMeta):
    name = SizedString(size=8)
    shares = UnsignedInteger()
    price = UnsignedFloat()

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price


def test():
    print("test123")


if __name__ == '__main__':
    stock = Stock("ACME", 9, 10.1)
    print(stock.name)
    print(stock.price)
    # stock.price = 10

    stock1 = Stock1("ACME", 9, 10.1)
    print(stock1.name)

    NewClass = type("NewClass", (), {"test": test})
    NewClass.test()

    stock3 = Stock3("ACME", 1, 1.0)
    print(stock3.name)

