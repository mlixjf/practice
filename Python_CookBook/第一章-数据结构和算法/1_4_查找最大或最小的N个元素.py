import heapq
from heapq import nlargest, nsmallest

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(nlargest(2, nums))
print(nsmallest(4, nums))
portfolio = [
{'name': 'IBM', 'shares': 100, 'price': 91.1},
{'name': 'AAPL', 'shares': 50, 'price': 543.22},
{'name': 'FB', 'shares': 200, 'price': 21.09},
{'name': 'HPQ', 'shares': 35, 'price': 31.75},
{'name': 'YHOO', 'shares': 45, 'price': 16.35},
{'name': 'ACME', 'shares': 75, 'price': 115.65}
]

print(nlargest(2, portfolio, key=lambda data: data["shares"]))
print(sorted(portfolio, key=lambda data: data["shares"], reverse=True)[:2])

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(nums)
heapq.heapify(nums)
print(nums)

print(heapq.heappop(nums))
print(heapq.heappop(nums))
print(heapq.heappop(nums))

heapq.heappush()