prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

print(prices.keys())
print(prices.values())

print(min(zip(prices.values(), prices.keys())))
print(max(zip(prices.values(), prices.keys())))

reverse_prices = zip(prices.values(), prices.keys())
print(max(reverse_prices))

print(sorted(zip(prices.values(), prices.keys())))

print(min(prices, key=lambda k: prices[k]))

print(type(prices.keys()))
