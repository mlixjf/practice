import random

nums = [1, 2, 3, 4, 5]
print(random.choice(nums))
print(random.choice(nums))
print(random.choice(nums))

print(random.sample(nums, 2))
print(random.sample(nums, 2))

random.shuffle(nums)
print(nums)

print(random.randint(0, 3))
print(random.randint(0, 3))
print(random.randint(0, 3))
print(random.randint(0, 3))
print(random.randint(0, 3))

print(random.random())
print(random.random())
print(random.random())

print(random.getrandbits(4))