import datetime


class Date:

    def __init__(self, year: int, month: int, day: int) -> None:
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def today(cls):
        today = datetime.datetime.today()
        return cls(today.year, today.month, today.day)

    def __repr__(self):
        return "Date({0.year!r}, {0.month!r}, {0.day!r})".format(self)

    def __str__(self):
        return "(%s, %s, %s)" % (self.year, self.month, self.day)


class NewDate(Date):
    pass


if __name__ == '__main__':
    """类方法的作用就是用来创造构造器"""
    date = Date.today()
    print(date)

    newDate = NewDate.today()
    print(newDate)