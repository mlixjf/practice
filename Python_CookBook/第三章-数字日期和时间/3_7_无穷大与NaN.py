import math

a = float("inf")
b = float("-inf")
c = float("nan")

import numpy as np
print(a, b, c)
print(np.nan)
print(c == np.nan)

print(math.isinf(a))
print(math.isinf(b))

print(a + 45)
print(a * 10)
print(a / 10)
print(10 / a)

print(a / a)
b = float("inf")
print(a + b)
print(math.sqrt(float("nan")))

c = float("nan")
d = float("nan")
print(c == d)
print(c is d)
print(math.isnan(c))