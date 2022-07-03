from datetime import timedelta, datetime

a = timedelta(hours=5, minutes=10)
b = timedelta(hours=1)
c = a + b
print(c.days)
print(c.seconds)
print(c.total_seconds())

d = datetime(2022, 6, 30)
d2 = datetime(2022, 7, 31)
print(d2 - d)

print(d + a)