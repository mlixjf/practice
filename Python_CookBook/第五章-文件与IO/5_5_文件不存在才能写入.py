# with open("data/data.txt", "xt") as f:
#     f.write("123")

# with open("data/data3.txt", "xt") as f:
#     f.write("data3")

import os

if not os.path.exists("data/data3.txt"):
    with open("data/data3.txt", "wt") as f:
        f.write("dsfsdfsdf\n")
else:
    print("文件已经存在")