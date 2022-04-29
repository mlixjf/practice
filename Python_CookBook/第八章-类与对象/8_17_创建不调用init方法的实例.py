from time import localtime


class Date:

    def __init__(self, year: int, month: int,  day: int):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def today(cls):
        t = localtime()
        d = Date.__new__(Date)
        d.year = t.tm_year
        d.month = t.tm_mon
        d.day = t.tm_mday
        return d


if __name__ == '__main__':
    d = Date.__new__(Date)
    print(d)

    data = {"year": 2022, "month": 4, "day": 29}
    for key, value in data.items():
        setattr(d, key, value)

    print(d.year)
    d1 = Date.today()
    print(d1.year)