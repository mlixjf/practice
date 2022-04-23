# eg-1
def spam(a, b=42):
    print(a, b)


# eg-2
def spam_1(a, b=None):
    if b is None:
        b = []
    print(locals())


# eg-3
_no_value = object()


def spam_2(a, b=_no_value):
    if b is _no_value:
        print("no b value supplied")


# eg-4
x = 42


def spam_3(a, b=x):
    print(a, b)


# eg-5(error)
def spam_4(q, r=[]):
    print(r)
    return r


if __name__ == '__main__':
    print(spam.__defaults__)
    print(spam_1.__defaults__)
    print(isinstance(None, object))
    print("-" * 80)

    spam_2(1)
    spam_2(1, 2)
    spam_2(1, None)
    print("-" * 80)

    spam_3(1)
    print(spam_3.__defaults__)
    x = 23
    spam_3(1)
    print(spam_3.__defaults__)
    print("-" * 80)

    s = spam_4(1)
    print(spam_4.__defaults__)
    s.append(1)
    print(spam_4.__defaults__)
    s.append("hello")
    print(spam_4.__defaults__)
    z = spam_4(1)
    print("-" * 80)

    print(type(([],)))
