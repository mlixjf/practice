import logging
import time
from functools import wraps

analyze_logger = logging.getLogger("analyze_logger")
analyze_logger.setLevel(logging.INFO)
console = logging.StreamHandler()
console.setLevel(logging.INFO)
console.setFormatter(logging.Formatter("[%(message)s]"))
analyze_logger.addHandler(console)


def get_millis() -> int:
    """获取当前时间的毫秒值"""
    return int(time.time() * 1000)


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        begin = get_millis()
        result = func(*args, **kwargs)
        end = get_millis()
        print(time.time())
        analyze_logger.info(f"function:{func.__name__}, begin:{begin}, end:{end}, cost:{end - begin}ms")
        print(time.time())
        return result

    return wrapper


@timer
def test() -> None:
    time.sleep(0.1)


class Test(object):

    @timer
    def test(self):
          time.sleep(0.1)


def timestamp_to_str(timestamp: int) -> str:
    return datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]


def b(x, *args, y, **kwargs):
    print(locals())


if __name__ == '__main__':
    test()
    t = Test()
    t.test()

    from datetime import datetime

    t = datetime.fromtimestamp(1649648469)
    print(type(t))

    print(timestamp_to_str(1649648469))
