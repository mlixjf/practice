from singleton_by_module import singleton
#
# print(singleton.__dict__)
# print(singleton.name)
# singleton.name = "demo"

import py_compile


py_compile.compile("/Python_CookBook/精通python设计模式/单例模式/demo.py")

# np = __import__("numpy")
# print(np.nan)
import importlib
import _demo
import sys
from pprint import pprint
pprint(sys.modules)
print(sys.modules)
print("*" * 50)
print(sys.modules.get("numpy", None))

print(sys.modules.get("numpy"))
importlib.reload(_demo)
print(_demo.__spec__)
print(id(singleton))
print(id(singleton))