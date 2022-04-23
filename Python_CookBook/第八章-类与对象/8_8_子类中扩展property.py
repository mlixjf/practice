class Person(object):
    """Person"""

    def __init__(self, name: str) -> None:
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        if not isinstance(value, str):
            raise TypeError("类型错误")
        self._name = value

    @name.deleter
    def name(self):
        raise TypeError("不能删除此类型")


class SubPerson(Person):

    @property
    def name(self):
        print("Getting name")
        return super().name

    @name.setter
    def name(self, value: str):
        print('Setting name to', value)
        super(SubPerson, SubPerson).name.__set__(self, value)

    @name.deleter
    def name(self):
        print('Deleting name')
        super(SubPerson, SubPerson).name.__delete__(self)


class SubPersonNew(Person):

    @Person.name.getter
    def name(self):
        print("new name")
        return super().name


if __name__ == '__main__':
    p = Person("123")
    print(p.name)

    s = SubPerson("duosan")
    print(s.name)

    s1 = SubPersonNew("123")
    print(s1.name)