import errno

try:
    f = open("./test.txt", mode="rt")
except FileNotFoundError as e:
    print("文件打开失败")
    print(e)


try:
    f = open("./test.txt", mode="rt")
except IOError as e:
    if e.errno == errno.ENOENT:
        print(dir(e))
        print("file not found")