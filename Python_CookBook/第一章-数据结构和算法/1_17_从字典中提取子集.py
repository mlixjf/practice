prices = {
'ACME': 45.23,
'AAPL': 612.78,
'IBM': 205.55,
'HPQ': 37.20,
'FB': 10.75
}
p1 = {key: value for key, value in prices.items() if value > 200}
print(p1)
p3 = ((k, v) for k, v in prices.items() if v > 200)
print(dict(p3))
tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
p2 = {k: v for k, v in prices.items() if k in tech_names}
print(p2)