import inspect
from inspect import Signature, Parameter


def func(a, /, c, d=4, *, e=5, f):
    """

    :param a: POSITIONAL_ONLY
    :param c: POSITIONAL_OR_KEYWORD
    :param d: POSITIONAL_OR_KEYWORD
    :param e: KEYWORD_ONLY
    :param f: KEYWORD_ONLY
    :return:
    """
    pass


func(1, 2, 3, f=5)


def add(x, y):
    return x + y


params = [
    Parameter("x", Parameter.POSITIONAL_OR_KEYWORD, annotation="int"),
    Parameter("y", Parameter.POSITIONAL_OR_KEYWORD, default=42, annotation="int"),
    Parameter("z", Parameter.POSITIONAL_OR_KEYWORD, default=None, annotation="int")]

sig = Signature(params)


def func(*args, **kwargs):
    bound_values = sig.bind(*args, **kwargs)
    for name, value in bound_values.arguments.items():
        print(name, value)


def make_sig(*names):
    parms = [Parameter(name, Parameter.POSITIONAL_OR_KEYWORD) for name in names]
    return Signature(parms)


class Structure:
    __signature__ = make_sig()

    def __init__(self, *args, **kwargs):
        bound_values = self.__signature__.bind(*args, **kwargs)
        for name, value in bound_values.arguments.items():
            setattr(self, name, value)


class Stock(Structure):
    __signature__ = make_sig("name", "shares", "price")


class Point(Structure):
    __signature__ = make_sig("x", "y")


class StructureMeta(type):

    def __new__(cls, name, bases, clsdict):
        print("StructureMeta new execute")
        clsdict["__signature__"] = make_sig(*clsdict.get("_field"))
        return super().__new__(cls, name, bases, clsdict)


class NewStructure(metaclass=StructureMeta):
    _field = []

    def __init__(self, *args, **kwargs):
        bound_values = self.__signature__.bind(*args, **kwargs)
        for name, value in bound_values.arguments.items():
            setattr(self, name, value)


class NewStock(NewStructure):
    _field = ["name", "shares", "price"]


if __name__ == '__main__':
    # print(inspect.isfunction(add))
    # print(inspect.isclass(add))
    # print(inspect.getsourcelines(add))

    print(sig)
    func(1, 2, z=3)
    # func(1, 2, 3, 4)

    stock = Stock("ACME", 100, 9.1)
    print(stock.price)

    s = NewStock("ACME", 100, 9.1)
    print(s.price)