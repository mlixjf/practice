class Point(object):

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Point({0!r}, {1!r})".format(self.x, self.y)

    def __str__(self):
        return "({0!s}, {1!s})".format(self.x, self.y)


if __name__ == '__main__':
    p = Point(1.0, 1.0)
    print(p)
    print(repr(p))
    print(eval(repr(p)))
    print(eval(repr(p)) == p)
    p1 = eval(repr(p))
    print(p1 == p)
    print(1 == 1)