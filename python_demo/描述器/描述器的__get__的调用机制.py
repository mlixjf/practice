class M:

    def __init__(self):
        self.x = 1

    def __get__(self, instance, cls):
        return self.x

    def __set__(self, instance, value):
        self.x = value


class AA:

    m = M()
    n = 2

    def __init__(self, score):
        self.score = score


if __name__ == '__main__':
    aa = AA(3)
    print(aa.__dict__)
    print(aa.score)
    print(aa.__dict__["score"])

    print(type(aa).__dict__)
    print(aa.n)
    print(type(aa).__dict__["n"])

    print(aa.m)
    print(type(aa).__dict__["m"].__get__(aa, AA))

    print(AA.m)
    print(AA.__dict__["m"].__get__(None, AA))