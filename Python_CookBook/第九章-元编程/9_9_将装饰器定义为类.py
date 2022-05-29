import types
from functools import wraps


class Profiled:

    def __init__(self, func):
        wraps(func)(self)
        self.n_call = 0

    def __call__(self, *args, **kwargs):
        self.n_call += 1
        return self.__wrapped__(*args, **kwargs)

    def __get__(self, instance, cls):
        print("instance")
        if instance is None:
            return self
        else:
            return types.MethodType(self, instance)


@Profiled
def add(x, y):
    return x + y


class Spam:

    @Profiled
    def bar(self, x):
        print(self, x)


if __name__ == '__main__':
    add(1, 1)
    # print(add.n_call)
    # add(1, 2)
    # print(add.n_call)
    #
    # s = Spam()
    # s.bar(1)
    # print(s.bar.n_call)