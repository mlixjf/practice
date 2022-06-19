try:
    print(1 / 0)
except (Exception, RuntimeError):
    print("do something...")
    raise
