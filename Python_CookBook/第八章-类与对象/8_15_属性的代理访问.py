"""
代理：将某个对象的操作转移给另外的对象执行
"""
from typing import Union, Any


class A:

    def bar(self, value):
        print("A.bar执行", value)

    def foo(self, value):
        print("A.foo执行", value)


class B:

    def __init__(self):
        self._a = A()

    def bar(self, value):
        return self._a.bar(value)

    def foo(self, value):
        return self._a.foo(value)


class Proxy:

    def __init__(self, obj) -> None:
        self._obj = obj

    def __getattr__(self, name: str):
        return getattr(self._obj, name)

    def __setattr__(self, name: str, value: Any):
        if name.startswith("_"):
            super().__setattr__(name, value)
        else:
            setattr(self._obj, name, value)

    def __delattr__(self, name: str):
        if name.startswith("_"):
            super().__delattr__(name)
        else:
            delattr(self._obj, name)


class Spam:

    def __init__(self, x):
        self.x = x

    def spam(self, y):
        print("Spam的spam执行", y)


if __name__ == '__main__':
    spam = Spam(1)
    proxy = Proxy(spam)
    proxy.spam(1)