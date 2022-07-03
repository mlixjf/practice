data = {"name": "123"}
info = {"dsf": 1}

print({**data, **info})

from collections import namedtuple

Subscribers = namedtuple("Subscribers", ['addr', 'joined'])
sub = Subscribers("shanghai", "2022-7-3")
print(sub.addr)
print(sub.joined)
print(len(sub))

addr, joined = sub
print(addr, joined)

Stock = namedtuple("Stock", ["name", "shares", "price"])

data = [
    ['ACME', 100, 45.23],
    ['AAPL', 80, 612.78],
    ['IBM', 10, 205.55],
    ['HPQ', 200, 37.20],
    ['FB', 1000, 10.75]
]


def compute_cost(records):
    total = 0.0
    for record in records:
        stock = Stock(*record)
        total += stock.shares * stock.price

    return total


print(compute_cost(data))

s = Stock(*['ACME', 100, 45.23])
# s.name = "test"
print(s)
s1 = s._replace(price=23.90)
print(s1)

Stock = namedtuple("Stock", ["name", "shares", "price", "date", "time"])

stock_prototype = Stock("", 0, 0.0, None, None)


def dict_to_stock(d):
    return stock_prototype._replace(**d)


a = {'name': 'ACME', 'shares': 100, 'price': 123.45}
print(dict_to_stock(a))
