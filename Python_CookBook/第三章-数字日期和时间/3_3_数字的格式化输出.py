x = 1234.56789

print(format(x, "0.2f"))
print(format(x, ">10.2f"))
print(format(x, "<10.2f"))
print(format(x, "^10.2f"))
print(format(x, ","))
print(format(x, ".2e"))
print(format(x, ">2.2f"))
print(format(x, ",.1f"))

x = 12345.123418
print("x is {:^6,.3f}".format(x))
print(x.__format__("^20,.5f"))