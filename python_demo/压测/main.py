import importlib
import threading
from time import sleep

module = importlib.import_module("stg")


def run(count: int = 10000) -> None:
    for i in range(count):
        module.my_print(i)

all_thread = []
for i in range(9):
    t = threading.Thread(target=run)
    t.start()
    all_thread.append(t)

for thread in all_thread:
    thread.join()