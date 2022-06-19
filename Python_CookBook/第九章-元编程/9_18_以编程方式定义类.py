import abc


def __init__(self, name, shares, price):
    self.name = name
    self.shares = shares
    self.price = price


def cost(self):
    return self.shares * self.price


cls_dict = {
    "__init__": __init__,
    "cost": cost
}

import types

Stock = types.new_class("Stock", (), {}, lambda ns: ns.update(cls_dict))
print(type(Stock))
print(Stock)
Stock.__module__ = __name__
print(Stock)
print(type(Stock))

print(__name__)
s = Stock("ACME", 50, 9.1)
print(s.name)
S = type("Stock", (), cls_dict)
print(Stock.__module__)

s1 = S("ACME", 50, 9.1)
print(s1.name)
print(S.__module__)

NewStock = types.new_class("NewStock", (), {"metaclass": abc.ABCMeta},
                           lambda ns: ns.update(cls_dict))
NewStock.__module__ = __name__

print(type(NewStock))