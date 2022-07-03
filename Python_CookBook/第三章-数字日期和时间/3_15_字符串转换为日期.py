from datetime import datetime

date_string = "2022-06-30 22:02:34.123"

d = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S.%f")
print(d)

d1 = datetime.strftime(d, "%Y%m%d-%H:%M:%S.%f")
print(d1)
