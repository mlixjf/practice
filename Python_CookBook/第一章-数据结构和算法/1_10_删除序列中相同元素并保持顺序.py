def dedupe(items, key=None):
    seen = set()
    for item in items:
        value = item if key is None else key(item)
        if value not in seen:
            yield item
            seen.add(value)


a = [1, 5, 2, 1, 9, 1, 5, 10]
b = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]

print(list(dedupe(a)))

print(list(dedupe(b, key=lambda d: (d["x"], d["y"]))))