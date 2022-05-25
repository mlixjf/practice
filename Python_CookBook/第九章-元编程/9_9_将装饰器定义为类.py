import types

from functools import wraps


class Profiled:

    def __init__(self, func):
        wraps(func)(self)
        self.ncalls = 0

    def __call__(self, *args, **kwargs):
        print(locals())
        self.ncalls += 1
        return self.__wrapped__(*args, **kwargs)

    def __get__(self, instance, cls):
        print("instance", type(instance))
        if instance is None:
            return self
        else:
            print(self)
            print(type(self))
            print(types.MethodType(self, instance))
            return types.MethodType(self, instance)


@Profiled
def add(x, y):
    return x + y


class Spam:

    @Profiled
    def bar(self, x):
        print(self, x)


def profiled(func):
    ncalls = 0

    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal ncalls
        ncalls += 1
        return func(*args, **kwargs)

    wrapper.ncalls = lambda: ncalls
    return wrapper


@profiled
def add(x, y):
    return x + y


class Spam1:
    def bar(self):
        print("new bar")


if __name__ == '__main__':
    # print(add(2, 3))
    # print(add(1, 1))
    # print(add.ncalls)

    s = Spam()
    s.bar(1)
    print(Spam.bar.ncalls)

    print(Spam.__dict__["bar"].__get__(s, Spam))
    s1 = Spam1()
    print(Spam1.bar)
    print(s1.bar)
    # add(1, 1)
    # print(add.ncalls())