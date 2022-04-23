from functools import partial


def test(a, /, b):
    """/的用法：(3.8)
    如果你需要函数的参数的只能是位置参数，而不能是关键字参数，只需要在这个参数后面放上一个/（反斜杠），这个"/",
    不会对后面的参数有任何影响
    """
    print(a, b)


test(1, 2)
test(1, b=2)


# test(a=1, b=2)


def spam(a, b, c, d):
    print(a, b, c, d)
    print(type(locals()))


spam(1, 2, 3, 4)

s = partial(spam, 1)

points = [(1, 2), (3, 4), (5, 6), (7, 8)]

import math


def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.hypot(x2 - x1, y2 - y1)


pt = (4, 3)
points.sort(key=partial(distance, pt))
print(points)


def output_result(result, log=None):
    if log is not None:
        log.debug("Got: %r", result)


def add(x, y):
    return x + y


if __name__ == '__main__':
    import logging
    from multiprocessing import Pool
    from functools import partial

    logging.basicConfig(level=logging.DEBUG)
    log = logging.getLogger("test")

    p = Pool()
    p.apply_async(add, (3, 4), callback=partial(output_result, log=log))
    p.close()
    p.join()