nums = list(range(1, 6))

print([x * x for x in nums])
print(list(x * x for x in nums))
new_nums = map(lambda x: x * x, nums)
print(list(new_nums))

s = ('ACME', 50, 123.45)
print(":".join(str(v) for v in s))

