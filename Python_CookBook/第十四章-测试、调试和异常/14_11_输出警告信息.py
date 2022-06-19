import warnings


warnings.simplefilter("error")


def func(x, y, logfile=None, debug=False):
    if logfile is None:
        warnings.warn("logfile argument deprecated", DeprecationWarning)


func(1, 2)

f = open("raise.py", "rt", encoding="utf-8")
del f



