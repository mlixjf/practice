class Descriptor:

    def __init__(self, name, **opts):
        self.name = name
        for key, value in opts.items():
            setattr(self, key, value)

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value


def Typed(expected_type, cls=None):
    if cls is None:
        print("第一次进来")
        return lambda cls:  Typed(expected_type, cls)

    print("第二次进来， %s" % cls.__name__)
    super_set = cls.__set__

    def __set__(self, instance, value):
        if not isinstance(value, expected_type):
            raise TypeError("Expected %s" % str(expected_type))
        print("第三次进来， %s" % cls.__name__)
        super_set(self, instance, value)

    print("第四次进来， %s" % cls.__name__)
    cls.__set__ = __set__
    return cls


def Unsigned(cls):
    super_set = cls.__set__

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Expected >= 0")
        super_set(self, instance, value)

    cls.__set__ = __set__
    return cls


def MaxSized(cls):
    super_init = cls.__init__

    def __init__(self, name=None, **opts):
        if "size" not in opts:
            raise TypeError("missing size option")
        super_init(self, name, **opts)

    cls.__init__ = __init__

    super_set = cls.__set__

    def __set__(self, instance, value):
        if len(value) >= self.size:
            raise ValueError("size must be < " + str(self.size))
        super_set(self, instance, value)

    cls.__set__ = __set__
    return cls


@Typed(int)
class Integer(Descriptor):
    pass


@Unsigned
class UnsignedInteger(Integer):
    pass


@Typed(float)
class Float(Descriptor):
    pass


@Unsigned
class UnsignedFloat(Float):
    pass


@Typed(str)
class String(Descriptor):
    pass


@MaxSized
class SizedString(String):
    pass


class Stock:
    name = SizedString("name", size=8)
    share = UnsignedInteger("share")
    price = UnsignedFloat("price")

    def __init__(self, name, share, price):
        self.name = name
        self.share = share
        self.price = price


if __name__ == '__main__':

    stock = Stock("ACME", 1, 1.0)
    print(stock.name)
    print(stock.share)
    print(stock.price)

    stock.price = 2.0
