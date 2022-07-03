with open("data/\xf1o.txt", "w") as f:
    f.write("test")

import os

print(os.listdir("data"))

print(os.listdir(b"data"))
# os.listdir在输出的没有经过系统默认编码的文件名时，会进行自己的映射，python3.3的版本，
# 直接输出这个映射会有问题，3.9这个问题已经没有了

with open("data/ño.txt", "r") as f:
    print(f.read())

print(os.path.isfile(b"data/" + b'\xc3\xb1o.txt'))