import threading
import time


class Singleton(object):
    _instance_lock = threading.Lock()

    def __init__(self):
        time.sleep(12)

    @classmethod
    def get_instance(cls):
        with Singleton._instance_lock:
            if not hasattr(Singleton, "_instance"):
                Singleton._instance = Singleton()
        return Singleton._instance


def task():
    print(Singleton.get_instance())


if __name__ == '__main__':
    s1 = Singleton.get_instance()
    # print(id(s1))
    s2 = Singleton.get_instance()
    # print(id(s2))

    for i in range(100):
        t = threading.Thread(target=task)
        t.start()
