try:
    print(1 / 0)
except ZeroDivisionError as e:
    raise ZeroDivisionError("0不可以做除数") from e
