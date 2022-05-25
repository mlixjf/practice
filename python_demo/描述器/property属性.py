class Person:

    def __init__(self, name: str) -> None:
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


class Student:

    def __init__(self, name: str) -> None:
        self.name = name

    def get_name(self):
        print("get name")
        return self._name

    def set_name(self, name):
        print("set name")
        self._name = name

    name = property(get_name, set_name)

    def test(self):
        print("test111")

    def test(self):
        print("test222")


if __name__ == '__main__':
    s = Student("111")
    print(s.name)
    s.name = 222
    print(s.name)
    print(s.test())
