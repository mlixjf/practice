import importlib

math = importlib.import_module("math")
print(math.sin(2))

some = importlib.import_module(".some", "some")
some.some()