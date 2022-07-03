from datetime import datetime
from pytz import timezone

d = datetime(2012, 12, 21, 9, 30, 0)
print(d)
central = timezone("US/Central")
loc_d = central.localize(d)
print(loc_d)

print(hex(1024))
print(int("16", 16))
x = 0x10
print(x)
print(format(x, "x"))

