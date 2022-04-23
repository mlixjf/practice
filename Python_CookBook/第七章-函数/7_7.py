x = 10


def add(y):
    r = x + y
    print(r)


x = 20


def add1(y):
    r = x + y
    print(r)


add(10)
add1(10)

x = 15
add(10)
add1(10)

x = 200
add(10)
add1(10)
print(add.__defaults__)

x = 10
a = lambda y, x=x: x + y
print(a(10))
x = 40
print(a(10))
print(a.__defaults__)


func = [lambda x: x + n for n in range(5)]
for f in func:
    print(f(0))

func_1 = [lambda x, n=n: x + n for n in range(5)]
for f in func_1:
    print(f(0))
