import threading


class Singleton(object):
    _instance_lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if not hasattr(Singleton, "_instance"):
            with Singleton._instance_lock:
                Singleton._instance = super().__new__(cls, *args, **kwargs)

        return Singleton._instance


def task(index: int) -> None:
    print(Singleton())


if __name__ == '__main__':

    for i in range(10):
        t = threading.Thread(target=task, args=(i,))
        t.start()
