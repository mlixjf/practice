def test():
    pass


add = lambda x, y: x + y
print(dir(add))
print(dir(test))
print(add(1, 2))

names = ['David Beazley', 'Brian Jones', 'Raymond Hettinger', 'Ned Batchelder']

lst = sorted(names, key=lambda name: name[0].lower())
print(lst)
