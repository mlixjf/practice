b1 = bytes("hello")
print(b1)

b2 = b"hello"
print(b2)

print(b1 == b2)
print(b1 is b2)

b3 = "hello".encode("utf-8")
print(b3)

b4 = "我喜欢你".encode("utf-8")
print(b4)

print(b4.decode("utf-8"))