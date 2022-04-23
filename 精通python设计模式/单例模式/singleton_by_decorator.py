def singleton(cls):
    _instance = {}
    count = 0

    def _inner(*args, **kwargs):
        nonlocal count
        if cls.__name__ not in _instance:
            print(f"count: {count} {cls.__name__} not init")
            _instance[cls.__name__] = cls(*args, **kwargs)
        else:
            count += 1
        return _instance[cls.__name__]

    return _inner


@singleton
class Test(object):

    def __init__(self, name):
        self.name = name


if __name__ == '__main__':
    t = Test("first")
    print(id(t))
    t2 = Test("secone")
    print(id(t2))

    d = {
        Test: 1
    }
    print(d)