import os

file_path = "data/data.txt"
print(os.path.basename(file_path))
print(os.path.dirname(file_path))
print(os.path.join("test", "data", os.path.basename(file_path)))
print(os.path.expanduser("~/Desktop"))
print(os.path.splitext(file_path))