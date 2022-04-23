class Test:

    def __next__(self):
        pass

from collections.abc import Iterator, Iterable

t = Test()
print(isinstance(t, Iterable))
print(isinstance(t, Iterator))