import bisect
from collections.abc import Iterator, Iterable, Sequence, MutableSequence
from typing import Any


class SortedItems(Sequence):

    def __init__(self, initial=None) -> None:
        self._items = sorted(initial) if initial is not None else []

    def __getitem__(self, index: int) -> Any:
        return self._items[index]

    def __len__(self) -> int:
        return len(self._items)

    def add(self, item):
        """bisect排序列表中，可以高效插入数据"""
        bisect.insort(self._items, item)


class Items(MutableSequence):

    def __init__(self, initial=None) -> None:
        self._items = sorted(initial) if initial is not None else []

    def __delitem__(self, index: int) -> None:
        del self._items[index]

    def __getitem__(self, index: int) -> Any:
        return self._items[index]

    def __len__(self) -> int:
        return len(self._items)

    def __setitem__(self, index: int, value: Any) -> None:
        self._items[index] = value

    def insert(self, index: int, value: Any) -> None:
        self._items.insert(index, value)


if __name__ == '__main__':
    items = SortedItems([1, 5, 3, 22, 1, 9, 3, 2, 0])
    print(list(items))
    items.add(6)
    print(list(items))
    print(isinstance(items, Iterable))
    print(isinstance(items, Iterator))

    # print(MutableSequence())

    items = Items([1, 2, 3, 4])
    print(len(items))
    print(items[1:])
