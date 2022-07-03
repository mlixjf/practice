from collections import ChainMap
a = {'x': 1, 'z': 3 }
b = {'y': 2, 'z': 4 }

c = ChainMap(a, b)
print(c["x"])
print(c["z"])
print(c["y"])
c["z"] = 2222
print(a, b)