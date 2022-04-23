class Date(object):
    """my Date"""
    __slots__ = ["year",  "day", "month"]  # __slots__的主要作用是来优化内存

    def __init__(self, year: int, month: int, day: int) -> None:
        self.year = year
        self.month = month
        self.day = day


class Test(Date):
    pass


if __name__ == '__main__':
    d = Date(2022, 4, 15)
    print(dir(d))
    print(d.year, d.month, d.day)

    t = Test(2022, 4, 15)
    print(t.year)