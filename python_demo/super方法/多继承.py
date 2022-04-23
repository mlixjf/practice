class Base(object):

    def __init__(self):
        print("I am Base")


class A(Base):

    def __init__(self):
        Base.__init__(self)
        print("I am A")


class B(Base):

    def __init__(self):
        Base.__init__(self)
        print("I am B")


class C(A, B):

    def __init__(self):
        A.__init__(self)
        B.__init__(self)
        print("I am C")


if __name__ == '__main__':
    c = C()