a = 13
exec("b = a + 1")
print(b)
print("locals: %s" % locals())
print("global: %s" % globals())


def test():
    a = 13
    exec("b = a + 1")
    print(b)

test()
