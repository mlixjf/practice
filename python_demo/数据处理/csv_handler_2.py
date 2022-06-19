import csv
import json
from datetime import datetime


def std_to_data(date_time, std_fmt="%Y%m%d-%H:%M:%S.%f", data_fmt="%Y-%m-%d %H:%M:%S") -> str:
    """%Y%m%d-%H:%M:%S -> %Y-%m-%d %H:%M:%S"""
    return datetime.strptime(date_time, std_fmt).strftime(data_fmt)


des_csv = csv.writer(open(file="./T2136.csv", mode="wt", encoding="utf-8", newline=""))

with open(file="./my_csv/SM00202206100014_T2136.csv", mode="rt", encoding="utf-8") as f:
    for line in f:
        data = json.loads(line)
        source_data = data["body"]["fields"]
        print(source_data["TRANSACTTIME"])
        # print(std_to_data(source_data["TRANSACTTIME"]))
        des_csv.writerow([std_to_data(source_data["TRANSACTTIME"]),
                          source_data["LASTPX_HIGH"],
                          source_data["LASTPX_OPEN"],
                          source_data["LASTPX_LOW"],
                          source_data["LASTPX_CLS"],
                          source_data["CUM_VOLUME_TRADED"],
                          ], )
