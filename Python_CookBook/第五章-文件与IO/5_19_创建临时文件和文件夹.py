import tempfile
from tempfile import TemporaryFile, NamedTemporaryFile, TemporaryDirectory

with TemporaryFile("w+t") as f:
    f.write("test")


with NamedTemporaryFile("w+t") as f:
    print("filename is:", f.name)


with TemporaryDirectory() as dirname:
    print(dirname)

print(tempfile.gettempdir())

print(tempfile.mkstemp())