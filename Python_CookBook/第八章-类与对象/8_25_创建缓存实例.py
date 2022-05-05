import weakref


class Spam:
    def __init__(self, name: str) -> None:
        self.name = name


_spam_cache = weakref.WeakValueDictionary()


def get_spam(name: str):
    if name not in _spam_cache:
        spam = Spam(name)
        _spam_cache[name] = spam
        return spam
    else:
        return _spam_cache[name]


if __name__ == '__main__':
    a = get_spam("foo")
    b = get_spam("bar")
    c = get_spam("foo")
    print(a is b)
    print(list(_spam_cache))
    del a
    del b
    print(list(_spam_cache))
    del c
    print(list(_spam_cache))
