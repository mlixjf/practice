import pickle

PATH = "data/data"

f = open(PATH, "wb")
pickle.dump({"data": "test"}, f)
f.close()

f1 = open(PATH, "rb")
data = pickle.load(f1)
f1.close()
print(data)

s = pickle.dumps("data")
print(s)
d = pickle.loads(s)
print(d)

f = open("somedata", "wb")
pickle.dump([1, 2, 3, 4], f)
pickle.dump("hello", f)
pickle.dump({"apple", "pear", "banana"}, f)
f.close()
f = open("somedata", "rb")
print(pickle.load(f))
print(pickle.load(f))
print(pickle.load(f))

import math

dat = pickle.dumps(math.sqrt)
sqrt = pickle.loads(dat)
print(sqrt(4))