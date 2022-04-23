import json
from dataclasses import dataclass
from datetime import datetime
from functools import wraps
from typing import Dict


def cache(func):
    cache_rate = "-1"

    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal cache_rate
        if cache_rate != kwargs["rate"]:
            cache_rate = kwargs["rate"]
            return func(*args, **kwargs)

    return wrapper


@cache
def send_to_cquant_service(msg: str, instance_id: str, *, rate) -> None:
    print("send msg: %s, second:%s, rate: %s" % (msg, instance_id, rate))


def get_rate(data_count: int) -> str:
    rate = (data_count / total_count) * 100
    print(rate)
    return str(int(rate))


@dataclass
class TimerData(object):
    trigger_time: str
    comments: str
    month: int = 1
    weekday: int = 1
    day: int = 1
    hour: int = 0
    minute: int = 0
    second: int = 0

    def __post_init__(self):
        temp_time = datetime.strptime(self.trigger_time, "%Y-%m-%d %H:%M:%S")
        self.month, self.weekday, self.day, self.hour, self.minute, self.second = (temp_time.month,
                                                                                   temp_time.weekday() + 1,
                                                                                   temp_time.day,
                                                                                   temp_time.hour,
                                                                                   temp_time.minute,
                                                                                   temp_time.second)


def std_to_normal(date_time) -> str:
    """%Y%m%d-%H:%M:%S.%f -> %Y-%m-%d %H:%M:%S.%f"""
    return datetime.strptime(date_time, "%Y%m%d-%H:%M:%S").strftime("%Y-%m-%d %H:%M:%S")


def parse_timer(data: Dict[str, str]):
    """解析定时器数据"""
    return TimerData(trigger_time=std_to_normal(data["TRIGGERTIME"]), comments=data["COMMENTS"])


if __name__ == '__main__':
    total_count = 1200
    for i in range(1, 1201):
        send_to_cquant_service(get_rate(i), i, rate=get_rate(i))

    print(datetime.fromtimestamp(1650374322))

    data = '{"TIMER":{"MONTH":"5","WEEKDAY":"3","HOUR":"9","CUSNUMBER":"","COMMENTS":"","MODELID":"","MINUTE":"5","SECOND":"0","DAY":"12","TRIGGERTIME":"20210512-09:05:00"}}'
    print(parse_timer(json.loads(data)["TIMER"]))