a = 1


def func():
    global a
    a += 1
    b = 4

    def inner_func():
        nonlocal b
        b += 1
        print(b)

    inner_func()
    print(a)


if __name__ == '__main__':
    func()
    print(a)
