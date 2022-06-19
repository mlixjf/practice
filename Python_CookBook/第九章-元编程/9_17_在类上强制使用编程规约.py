import logging
from inspect import signature


class NoMixedCaseMeta(type):

    def __new__(cls, clsname, bases, clsdict):
        for name in clsdict:
            if name.lower() != name:
                raise TypeError("Bad attribute name: " + name)
        return super().__new__(cls, clsname, bases, clsdict)


class Root(metaclass=NoMixedCaseMeta):
    pass


class A(Root):

    def foo_bar(self):
        pass


# class B(Root):
#
#     def fooBar(self):
#         pass


def test():
    pass


class A:
    def test(self):
        print("A")


class B(A):
    def test(self):
        print("B")


class C(A):
    def test(self):
        print("C")


class D(B, C):
    def test(self):
        print("D")


print(super(D, D).__dict__)
super(D, D).test(B())


class MatchSignaturesMeta(type):

    def __init__(self, clsname, bases, clsdict):
        super().__init__(clsname, bases, clsdict)
        sup = super(self, )
        for name, value in clsdict.items():
            if name.startswith("_") or not callable(value):
                continue
            sup_method = getattr(sup, name, None)
            if sup_method:
                sig = signature(sup_method)
                sig1 = signature(value)
                if sig != sig1:
                    logging.warning('Signature mismatch in %s. %s != %s',
                                    value.__qualname__, sig, sig1)


class Root(metaclass=MatchSignaturesMeta):

    def bar(self, x, y, z):
        pass

    def foo(self, x, *, y):
        pass


class M(Root):

    def bar(self, x, y, z):
        pass

    def foo(self, x, y):
        pass
