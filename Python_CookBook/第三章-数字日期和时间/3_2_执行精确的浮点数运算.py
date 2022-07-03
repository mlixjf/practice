from decimal import Decimal, localcontext

a = 4.2
b = 2.1
print(a + b)

decimal_a = Decimal("4.2")
decimal_b = Decimal("21.12")
print(decimal_a + decimal_b)

with localcontext() as ctx:
    ctx.prec = 302
    print(decimal_a / decimal_b)


nums = [1.23e+18, 1, -1.23e+18]
print(sum(nums))
import math

print(math.fsum(nums))