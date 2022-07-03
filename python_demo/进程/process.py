import os
from multiprocessing import Process
from time import sleep


def countdown(n):
    while n > 0:
        print(os.getpid(), n)
        n -= 1
        sleep(1)


if __name__ == '__main__':
    for i in range(2):
        p = Process(target=pvm_worker.main, args=(100,))
        p.start()
