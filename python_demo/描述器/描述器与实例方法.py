class Descriptor:

    def __init__(self, name):
        self._name = name

    def __get__(self, instance, cls):
        print("Descriptor")
        return instance.__dict__[self._name]


class Test:
    name = Descriptor("name")

    def __init__(self, name):
        self.name = name

    def bar(self):
        print("bar execute...")


def bar():
    pass


if __name__ == '__main__':
    print(Test.bar)
    print(Test("123").bar)
    print(bar)
    print(Test)

    t = Test(111)
    print(t.name)

    print(Test.__dict__["bar"].__get__(t, Test))