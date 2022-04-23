from typing import Any


def apply_async(func, args, *, callback):
    result = func(*args)
    return callback(result)


def print_result(result):
    print("Got:", result)


def add(x, y):
    return x + y


class ResultHandler(object):

    def __init__(self) -> None:
        self.sequence = 0

    def handle(self, result: Any) -> None:
        self.sequence += 1
        print("[{}] Got {}".format(self.sequence, result))


def make_handler():
    sequence = 0

    def handler(result):
        nonlocal sequence
        sequence += 1
        print("[{}] Got {}".format(sequence, result))

    return handler


def make_handler1():
    sequence = 0
    while True:
        result = yield
        sequence += 1
        print("[{}] Got {}".format(sequence, result))


def handler_3(r, seq):
    print("[{}] Got {}".format(seq, r))


if __name__ == '__main__':
    apply_async(add, (3, 4), callback=print_result)

    handler = ResultHandler()
    apply_async(add, (3, 4), callback=handler.handle)

    handler = make_handler()
    apply_async(add, (3, 4), callback=handler)

    handler1 = make_handler1()
    next(handler1)
    apply_async(add, (3, 4), callback=handler1.send)

    seq = 1
    apply_async(add, (2, 3), callback=lambda r: handler_3(r, seq))

