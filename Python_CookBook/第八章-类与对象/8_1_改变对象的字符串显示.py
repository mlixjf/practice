class Pair(object):
    """"""

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    # !r 是一种格式化输出
    # "Pair({0.x!r}, {0.y!r})".format(self) 等价于 "Pari(%r, %r)" % (self.x, self.y)
    def __repr__(self):
        return "Pari(%r, %r)" % (self.x, self.y)

    def __str__(self):
        return "({0.x!s}, {0.y!s})".format(self)


if __name__ == '__main__':
    p = Pair(1, 1)
    print(repr(p))
    print(p)  # print(str(p))

