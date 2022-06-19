def spam():
    pass


def grok():
    pass


def _test():
    pass


def __test():
    pass


blah = 42

__all__ = ["spam", "grok"]


class A:
    __name = "A"


class B(A):
    pass


print(A.__dict__)
print(B.__dict__)
