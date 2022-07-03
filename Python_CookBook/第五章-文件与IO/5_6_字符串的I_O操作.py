from io import StringIO, BytesIO

write_io = StringIO()
write_io.write("Hello\nWorld\n")
print(write_io.getvalue())


read_io = StringIO("Hello\nWorld\n")
print(read_io.read())

bytes_io = BytesIO()
bytes_io.write("new".encode("utf-8"))
print(bytes_io.getvalue().decode("utf-8"))