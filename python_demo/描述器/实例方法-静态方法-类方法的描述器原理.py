class A:

    @classmethod
    def print_classname(cls):
        print("classmethod")

    @staticmethod
    def print_staticname():
        print("staticmethod")

    def print_name(self):
        print("instance")


a = A()

a.print_classname()
a.print_staticname()
a.print_name()
print(a.__dict__)

print(A.__dict__["print_classname"])
print(a.print_classname)

print(A.__dict__["print_staticname"])
print(a.print_staticname)

print(A.__dict__["print_name"])
print(a.print_name)