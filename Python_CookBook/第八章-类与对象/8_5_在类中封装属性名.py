class A(object):
    """
    大多数情况应该使你的类的非公共属性以单下划线"_"开头,但是如果设计到子类，才会考虑以以双下划线开头
    """
    def __init__(self) -> None:
        self._internal = 0
        self.public = 1

    def public_method(self) -> None:
        """
        A public method
        :return:
        """
        pass

    def _private_method(self) -> None:
        """
        A private method
        :return:
        """


class B(object):
    """test"""

    def __init__(self) -> None:
        self.__private = 0

    def __private(self) -> None:
        """
        A private method
        :return:
        """
        pass


class C(B):
    def __init__(self):
        super().__init__()
        print(self.__private)

    def __private_method(self):
        pass


if __name__ == '__main__':

    a = A()
    a._internal = 2
    print(a.__dict__)
    print(dir(a))

    b = B()
    print(dir(b))

    c = C()
    # print(dir(c))
    # c._C_private = 2
    # print(c.__dict__)
