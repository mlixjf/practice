import time

from contextlib import contextmanager


@contextmanager
def timethis(label):
    start = time.time()
    try:
        yield
    finally:
        end = time.time()
        print("{} cost {}".format(label, end - start))


with timethis("counting") as x:
    n = 100000
    while n > 0:
        n -= 1


@contextmanager
def list_transactions(orig_list):
    working = list(orig_list)
    print(id(working))
    yield working
    orig_list[:] = working


items = [1, 2, 3]


with list_transactions(items) as working:
    working.append(4)
    working.append(5)
    print(id(working))


with list_transactions(items) as working:
    working.append(6)
    working.append(7)
    raise RuntimeError("opps")
