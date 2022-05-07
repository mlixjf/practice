from functools import wraps


class A:

    def decorator1(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print("decorator1执行")
            return func(*args, **kwargs)

        return wrapper

    @classmethod
    def decorator2(cls, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print("decorator2执行")
            return func(*args, **kwargs)

        return wrapper


a = A()


@a.decorator1
def add(x, y):
    return x + y


@A.decorator2
def spam():
    print("spam执行中")


class Person:
    first_name = property()

    @first_name.getter
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, name):
        if not isinstance(name, str):
            TypeError("Expected a string")
        self._first_name = name


if __name__ == '__main__':
    print(add(1, 2))
    spam()
