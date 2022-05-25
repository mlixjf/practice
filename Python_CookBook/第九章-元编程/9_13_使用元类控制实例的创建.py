import weakref


class NoInstances(type):

    def __call(cls, *args, **kwargs):
        raise TypeError("Can't instantiate directly")


class Spam(metaclass=NoInstances):

    @staticmethod
    def grok(x):
        print("Spam.grok")


class Singleton(type):

    def __init__(cls, *args, **kwargs):
        super().__init__(*args, **kwargs)
        cls.__instance = None

    def __call__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__call__(*args, **kwargs)
        return cls.__instance


class A(metaclass=Singleton):

    def __init__(self):
        pass


class Cached(type):

    def __init__(cls, *args, **kwargs):
        super().__init__(*args, **kwargs)
        cls.__cache = weakref.WeakValueDictionary()

    def __call__(cls, *args):
        for arg in args:
            if arg in cls.__cache:
                return cls.__cache[arg]
            else:
                obj = super().__call__(*args)
                cls.__cache[arg] = obj
                return obj


class Test(metaclass=Cached):
    def __init__(self, name):
        self.name = name


if __name__ == '__main__':
    Spam.grok(1)
    # s = Spam()

    a = A()
    b = A()
    print(a is b)
    x = None
    y = None
    print(x is y)

    t1 = Test("t1")
    t2 = Test("t2")
    t3 = Test("t1")

    print(t1 is t2)
    print(t1 is t3)

