from abc import ABCMeta, abstractmethod


class IStream(metaclass=ABCMeta):

    @abstractmethod
    def read(self, maxbytes=-1):
        pass

    @abstractmethod
    def write(self, data):
        pass


class SocketStream(IStream):

    def read(self, maxbytes=-1):
        pass

    def write(self, data):
        pass


def serialize(obj, stream):
    if not isinstance(stream, IStream):
        raise TypeError("Expected an IStream")
    pass


import io

IStream.register(io.IOBase)

f = open("foo.txt", mode="wt")

print(isinstance(f, IStream))