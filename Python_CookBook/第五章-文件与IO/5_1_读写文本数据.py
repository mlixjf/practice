import sys


def only_read():
    # r 只读模式，文件不存在会报错
    with open("data/data1.txt", "rt+", encoding="ascii", errors="replace") as f:
        for line in f:
            print(line)


def only_write():
    # w 只写模式，文件不存在会创建文件。如果文件存在，写入文件会覆盖之前的文件。
    with open("data/data.txt", "w") as f:
        f.write("123")


def only_append():
    # a: 相较于w模式，往已存在的文件写入时，会写在文件末尾（不换行），不会覆盖重写
    with open("data/data1.txt", "a") as f:
        f.write("123")
        print(f.tell())


def only_x():
    # x: 相较于w模式，文件不存在会报错。写入文件从头开始（适用于新增文件写入）
    with open("data/data2.txt", "x") as f:
        f.write("xxx")


if __name__ == '__main__':
    # print(sys.getdefaultencoding())
    only_read()
    # only_write()
    # only_append()
    # only_x()
