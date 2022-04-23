class Person(object):

    def __init__(self, first_name: str) -> None:
        self.first_name = first_name

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value: str):
        if not isinstance(value, str):
            raise TypeError("Expected a string")
        self._first_name = value

    @first_name.deleter
    def first_name(self):
        raise AttributeError("Can't delete attribute")


if __name__ == '__main__':
    p = Person("test")
    p.first_name = "123"
    print(p.__dict__)

    del p.first_name