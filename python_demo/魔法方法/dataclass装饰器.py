from dataclasses import dataclass


@dataclass
class Number(object):
    value: int


if __name__ == '__main__':
    num = Number()
    print(num)