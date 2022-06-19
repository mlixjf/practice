def demo1():
    with open("./data", "rt", encoding="utf-8", newline="") as f:
        while True:
            try:
                line = next(f)
                print(line, end="")
            except StopIteration:
                pass


def demo2():
    with open("./data", "rt", encoding="utf-8") as f:
        while True:
            line = next(f, None)
            if line is None:
                break
            print(line, end="")


if __name__ == '__main__':
    # demo1()
    demo2()
    items = [1, 2, 3]
    print(dir(items))
    it = iter(items)
    print(next(it))
    print(next(it))
    print(next(it))
    print(next(it))