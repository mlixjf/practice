def log_getattribute(cls):
    old_getattribute = cls.__getattribute__

    def new_getattribute(self, name):
        print("greet", name)
        return old_getattribute(self, name)

    cls.__getattribute__ = new_getattribute
    return cls


@log_getattribute
class A:

    def __init__(self, x):
        self.x = x

    def spam(self):
        pass


if __name__ == '__main__':
    a = A(1)
    print(a.x)
    a.spam()