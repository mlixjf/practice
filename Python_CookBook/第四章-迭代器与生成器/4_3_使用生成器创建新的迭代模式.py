def frange(start, stop, step):
    x = start
    while x < stop:
        yield x
        x += step


def countdown(n):
    print("Staring n".format(n))
    while n > 0:
        yield n
        n -= 1
    print("Done")


if __name__ == '__main__':
    for i in frange(1, 10, 2):
        print(i)

    n = countdown(3)
    print(next(n))
    print(next(n))
    print(next(n))
    print(next(n))