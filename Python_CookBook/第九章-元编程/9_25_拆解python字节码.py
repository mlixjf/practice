import dis
from datetime import datetime


def countdown(n):
    while n > 0:
        n -= 1
    print("Blastoff")


if __name__ == '__main__':
    dis.dis(countdown)

    print(datetime.strptime("2022-06-01 10:54:20.440", "%Y-%m-%d %H:%M:%S.%f").timestamp())

