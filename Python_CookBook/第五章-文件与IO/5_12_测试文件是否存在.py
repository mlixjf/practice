import os

print(os.path.exists("data"))
print(os.path.exists("data/data1.data"))
PATH = "data/data.txt"
print(os.path.isfile(PATH))
print(os.path.isdir(PATH))
print(os.path.islink(PATH))
print(os.path.relpath(PATH))
print(os.path.getsize(PATH))
