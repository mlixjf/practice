import inspect


class Person(object):

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str) -> None:
        self.name = name


def add(x: int, y: int) -> int:
    return x + y

if __name__ == '__main__':
    print(inspect.getmembers(Person))
    p = Person("Bob", 25)
    print("-" * 100)
    print(inspect.getmembers(p))

    sig = inspect.signature(add)
    print(sig)
    print(sig.return_annotation)
    print(sig.parameters)
    print(dir(sig.parameters["x"]))
    print(sig.parameters["x"].kind)
    print(sig.parameters["x"].name)
    print(sig.parameters["x"].default)
    print(sig.parameters["x"].annotation)