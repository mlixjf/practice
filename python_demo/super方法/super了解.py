class Test(object):

    def __init__(self, name: str) -> str:
        super()
        self.name = name


class Base(object):

    def greet(self):
        print("Hi, I am Base")


class A(Base):
    def greet(self):
        Base.greet(self)
        print("Hi, I am A")


if __name__ == '__main__':
    print(Test.__mro__)
    print(Test.mro())
    print(Test("123").__class__.mro())

    a = A()
    a.greet()