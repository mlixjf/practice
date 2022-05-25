import types


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def my_print(self):
        print("my_print")


def f1(self):
    print("f1")


p = Person("ming", 18)
p.my_print()
# p.f1 = types.MethodType(f1, p)
# p.f1()
t = types.MethodType(f1, p)
# t(1)

s = types.MethodType(Person.my_print, p)
s()