print("ACME", "50", 91.5)
print("ACME", "50", 91.5, sep="-")
print("ACME", "50", 91.5, sep="-", end="******")

for i in range(50):
    print(i)

for i in range(50):
    print(i, end="")

row = ("ACME", 50, 80)
print(".".join((str(s) for s in row)))

print(*row, sep="-")