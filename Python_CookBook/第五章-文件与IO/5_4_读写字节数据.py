with open("data/img.png", "rb") as f:
    print(f.read())

# with open("data/img.png", "rb") as r:
#     with open("data/img-1.png", "wb") as f:
#         for line in r:
#             for c in line:
#                 print(c)
#             f.write(line)

# with open("data/data.bin", "wb") as f:
#     text = "echo hello"
#     f.write(text.encode("utf-8"))


with open("data/data.bin", "rt") as f:
    data = f.read()


import array

nums = array.array("i", [1, 2, 3])
with open("data/data.bin", "wb") as f:
    f.write(nums)

a = array.array("i", [0,0,0,0,0])
with open("data/data.bin", "rb") as f:
    f.readinto(a)

print(a)