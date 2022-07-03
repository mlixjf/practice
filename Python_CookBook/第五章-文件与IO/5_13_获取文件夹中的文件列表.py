import os
from glob import glob
from fnmatch import fnmatch

PATH = "data/"
files = [name for name in os.listdir(PATH) if os.path.isfile(os.path.join(PATH, name))]
print(files)

dirs = [name for name in os.listdir(PATH) if os.path.isdir(os.path.join(PATH, name))]
print(dirs)

data_files = [name for name in os.listdir(PATH) if name.endswith(".data")]
print(data_files)

text_files = glob("data/*.txt")
print(text_files)

text_files = [text_file for text_file in os.listdir(PATH) if fnmatch(text_file, "*.txt")]
print(text_files)

text_files = glob("data/*.txt")
name_sz_data = [(text_file, os.path.getsize(text_file), os.path.getmtime(text_file))
                for text_file in text_files]
for item in name_sz_data:
    print(*item)

file_metadata = [(name, os.stat(name)) for name in text_files]
for name, meta in file_metadata:
    print(name, meta.st_size, meta.st_mtime)