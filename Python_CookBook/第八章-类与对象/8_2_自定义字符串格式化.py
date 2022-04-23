_formats = {
    "ymd": "{d.year}-{d.month}-{d.day}",
    "mdy": "{d.month}-{d.day}-{d.year}",
    "dmy": "{d.day}-{d.month}-{d.year}"
}


class Date(object):
    """my Date"""

    def __init__(self, year: int, month: int, day: int) -> None:
        self.year = year
        self.month = month
        self.day = day

    def __format__(self, format_spec):
        if format_spec == "":
            format_spec = "ymd"

        fmt = _formats[format_spec]
        return fmt.format(d=self)


if __name__ == '__main__':
    d = Date(2022, 4, 15)
    print(format(d))
    print(d.__format__(""))
    print(d.__format__("mdy"))
    print(f"{d}")
    print("{}".format(d))
    print("%s" % d)