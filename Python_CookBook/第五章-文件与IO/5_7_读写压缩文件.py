import gzip
import bz2

with gzip.open("data/data.gz", "wt", encoding="utf-8") as f:
    f.write("压缩文件测试")


with gzip.open("data/data.gz", "rt", encoding="utf-8") as f:
    print(f.read())


with bz2.open("data/data.bz2", "w") as f:
    f.write("bz2压缩测试".encode("utf-8"))

with bz2.open("data/data.bz2", "r") as f:
    print(f.read().decode("utf-8"))