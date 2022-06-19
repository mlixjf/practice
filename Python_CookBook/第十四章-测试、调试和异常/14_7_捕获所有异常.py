import sys
import traceback


def parse_int(s):
    try:
        i = int(s)
    except Exception:
        print(traceback.format_exc())

parse_int("a")
