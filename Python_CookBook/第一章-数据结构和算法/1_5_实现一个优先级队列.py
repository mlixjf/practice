import heapq


class PriorityQueue:

    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def poo(self):
        return heapq.heappop(self._queue)[-1]


class Item:

    def __init__(self, name):
        self._name = name

    def __repr__(self):
        return "Item({0._name!r})".format(self)


if __name__ == '__main__':
    q = PriorityQueue()
    q.push(Item("foo"), 1)
    q.push(Item("foo2"), 2)
    q.push(Item("foo3"), 3)
    q.push(Item("foo2-2"), 2)
    q.push(Item("foo5"), 5)
    print(q.poo())
    print(q.poo())
    print(q.poo())
    print(q.poo())
    print(q.poo())
