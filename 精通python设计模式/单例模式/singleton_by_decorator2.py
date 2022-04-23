from functools import wraps


def singleton(cls):
    _instance = {}

    def _singleton_wrapper(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls()
        return _instance[cls]

    return _singleton_wrapper


@singleton
class Test(object):

    def __init__(self, name):
        self.name = name


if __name__ == '__main__':
    t1 = Test()
    t2 = Test()
    print(id(t1))
    print(id(t2))
