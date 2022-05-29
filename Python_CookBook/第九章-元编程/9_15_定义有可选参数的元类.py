from abc import ABCMeta, abstractmethod

import synchronize as synchronize


class IStream(metaclass=ABCMeta):

    @abstractmethod
    def read(self, maxsize):
        pass

    @abstractmethod
    def write(self, data):
        pass


class MyMeta(type):

    @classmethod
    def __prepare__(cls, name, bases, *, debug, synchronize=False):
        print("prepare")
        return super().__prepare__(name, bases)

    def __new__(cls, name, bases, clsdict, *, debug=False, synchronize=False):
        print("new")
        return super().__new__(cls, name, bases, clsdict)

    def __init__(self, name, bases, clsdict, *, debug=False, synchronize=False):
        print("init")
        super().__init__(name, bases, clsdict)


class Spam(metaclass=MyMeta, debug=True, synchronize=True):
    pass


# if __name__ == '__main__':
#     s = Spam()