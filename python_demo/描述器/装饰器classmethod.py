class Myclassmethod:

    def __init__(self, method):
        self.method = method

    def __get__(self, instance, cls):
        return lambda *args, **kwargs: self.method(cls, *args, **kwargs)


class Mystaticmethod:

    def __init__(self, method):
        self.method = method

    def __get__(self, instance, cls):
        return self.method


class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @Myclassmethod
    def create(cls, name, age):
        return cls(name, age)

    @Mystaticmethod
    def test(name, age):
        print(name, age)

    def __repr__(self):
        return "Student(name={0.name!r},age={0.age!r})".format(self)


if __name__ == '__main__':
    s = Student.create("小明", 18)
    print(s)
    Student.test(1, 2)
    print(Student)
    print(type(s) == Student)