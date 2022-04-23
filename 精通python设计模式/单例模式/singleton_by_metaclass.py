import threading


class Singleton(type):

    _instance_lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            with Singleton._instance_lock:
                cls._instance = super().__call__(*args, **kwargs)
        return cls._instance


class Test(metaclass=Singleton):

    pass


if __name__ == '__main__':
    t1 = Test()
    t2 = Test()
    t1.name = "test"
    print(t1.__dict__)
    print(t2.__dict__)
