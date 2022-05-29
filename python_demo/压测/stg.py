from threading import *

file = open(file="./test.txt", mode="wt")

lock = Lock()
def my_print(msg):
    lock.acquire()
    print("thread:{}, msg:{}%".format(current_thread(), msg), file=file)
    lock.release()
