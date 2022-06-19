from collections.abc import Iterator


class Node:

    def __init__(self, value):
        self._value = value
        self._children = []

    def __iter__(self):
        # return iter(self._children)
        return self._children.__iter__()

    def __repr__(self):
        return "Node({!r})".format(self._value)

    def add_child(self, child):
        self._children.append(child)


if __name__ == '__main__':
    root = Node(0)
    child_1 = Node(1)
    child_2 = Node(2)
    root.add_child(child_1)
    root.add_child(child_2)

    for child in root:
        print(child)
    print(isinstance(root, Iterator))