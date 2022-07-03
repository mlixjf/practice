# 从python3.6以后python的字典（dict）就是有序的（字典添加key的顺序），
import json

import jsom as jsom

data = {}
data[1] = 1
data[2] = 2
data[3] = 3

# 字典的元素按插入的顺序排序
for k, v in data.items():
    print(k, v)

from collections import OrderedDict

d = OrderedDict()
d[1] = 1
d[2] = 2
d[3] = 3
for k, v in d.items():
    print(k, v)

print(json.dumps(d, ensure_ascii=False))
print(json.dumps(d))