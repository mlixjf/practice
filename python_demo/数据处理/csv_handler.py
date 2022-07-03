import csv
import json
import time
from datetime import datetime


def std_to_data(date_time, std_fmt="%Y%m%d-%H:%M:%S.%f", data_fmt="%Y-%m-%d %H:%M:%S") -> str:
    """%Y%m%d-%H:%M:%S -> %Y-%m-%d %H:%M:%S"""
    return datetime.strptime(date_time, std_fmt).strftime(data_fmt)


des_csv = csv.writer(open(file="./990002.csv", mode="wt", encoding="utf-8", newline=""))
with open(file="./my_csv/SM00202206100014_990002.csv", mode="rb") as f:
    for line in f:
        print(line)
#         data = json.loads(line)
#         source_data = data["body"]["fields"]
#         print(source_data)
#         des_csv.writerow([std_to_data(source_data["TRANSACTTIME"]),
#                           source_data["LASTPX_HIGH"],
#                           source_data["LASTPX_OPEN"],
#                           source_data["LASTPX_LOW"],
#                           source_data["LASTPX_CLS"],
#                           source_data["CUM_VOLUME_TRADED"],
#                           ], )
# print(time.time())
