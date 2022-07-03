record = '....................100 .......513.25 ..........'

SHARES = slice(20, 23)
PRICE = slice(31, 37)

cost = int(record[SHARES]) * float(record[PRICE])
print(cost)

a = slice(5, 50, 2)
print(a.start)
print(a.stop)
print(a.step)

s = "HelloWorld"
a.indices(len(s))
for i in range(*a.indices(len(s))):
    print(s[i])