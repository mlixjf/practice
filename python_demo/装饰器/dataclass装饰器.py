import dataclasses
import random
import time
from dataclasses import dataclass, field
from datetime import datetime
from typing import List


@dataclass
class InventoryItem(object):
    name: str
    unit_price: float
    quantity_on_hand: int = 0


@dataclass
class C(object):
    a: int
    b: int
    c: int = dataclasses.field(init=False)

    def __post_init__(self):
        self.c = self.a + self.b


def get_random_marks():
    return [random.randint(1, 10) for _ in range(10)]


@dataclass
class Student(object):
    marks: List[int]

    def __post_init__(self):
        self.marks = get_random_marks()


@dataclass(order=False)
class StudentNew(object):
    marks: List[int] = field(default_factory=get_random_marks)


@dataclass
class Person(object):
    name: str
    age: int


@dataclass
class Student1(Person):
    grade: float


def format_date(timeStamp: str):
    if timeStamp is None:
        return None
    if len(str(timeStamp)) == 13:
        timeStamp = int(timeStamp) / 1000
    d = datetime.fromtimestamp(timeStamp)
    format = "%Y-%m-%d %H:%M:%S.%f"
    d.strftime(format)
    return d.strftime(format)[:-3]


if __name__ == '__main__':
    c = C(1, 2)
    print(c)

    s1 = Student([21, 23, 3, 4, 5])
    print(s1)

    s2 = StudentNew()
    print(s2)
    print(dir(s2))
    s2.marks = [1, 2, 3]

    s1 = Student1("ds", 21, 100)
    print(s1.__dict__)

    t = int(time.time())
    print(type(format_date(t)))
