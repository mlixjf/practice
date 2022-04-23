#
# singleton.name = "test"
print("单例属性已修改")
print(dir())
# from singleton_by_module import singleton as singe

m = __import__("singleton_by_module")
singe = m.singleton
print(singe.__dict__)
print(dir())
