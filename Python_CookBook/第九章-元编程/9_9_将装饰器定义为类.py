import json
import types
from functools import wraps, partial


class MyCall:

    def __init__(self):
        self._call = 0

    def __call__(self, a, b):
        self._call += 1
        print(locals())


class Profiled:

    def __init__(self, func):
        wraps(func)(self)
        self.n_call = 0

    def __call__(self, *args, **kwargs):
        print("locals", locals())
        self.n_call += 1
        return self.__wrapped__(*args, **kwargs)

    def __get__(self, instance, cls):
        print("instance", instance, self)
        if instance is None:
            return self
        else:
            print(types.MethodType(self, instance))
            return types.MethodType(self, instance)  # 这里是把这个


@Profiled
def add(x, y):
    return x + y


class Spam:

    @Profiled
    def bar(self, x):
        print(self, x)


def test(self, x):
    print(type(self))
    print(self, x)


class Foo:

    def bar(self):
        pass


if __name__ == '__main__':
    # add.__call__(1, 2)
    # add(1, 1)
    # print(add.n_call)
    # add(1, 2)
    # print(add.n_call)
    #
    s = Spam()
    print(s.bar)
    # s.bar(1)
    # print(s.bar.n_call)
    # print(Spam.__dict__["bar"])
    # print(test)
    # s = types.MethodType(test, s)
    # print(s)
    # s(1)

    foo = Foo()
    method = foo.bar
    print(type(method) == types.MethodType)

    my_call = MyCall()
    s2 = types.MethodType(my_call, s)
    s2(1)

    date_string = json.loads("NONE")["transact_time"]
