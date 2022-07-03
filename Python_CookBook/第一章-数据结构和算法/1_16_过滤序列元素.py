from itertools import compress

mylist = [1, 4, -5, 10, -7, 2, 3, -1]

print([n for n in mylist if n > 0])

lst = (n for n in mylist if n > 0)
print(list(lst))
values = ['1', '2', '-3', '-', '4', 'N/A', '5']


def is_int(value):
    try:
        int(value)
        return True
    except ValueError as e:
        print("value is not int type!")
        return False


nums = filter(is_int, values)
print(list(nums))
lst = [1, None, 2, None]
print("**", list(filter(None, lst)))
print([n if n > 0 else 0 for n in mylist])

addresses = [
    '5412 N CLARK',
    '5148 N CLARK',
    '5800 E 58TH',
    '2122 N CLARK',
    '5645 N RAVENSWOOD',
    '1060 W ADDISON',
    '4801 N BROADWAY',
    '1039 W GRANVILLE',
]
counts = [0, 3, 10, 4, 1, 7, 6, 1]

more5 = [n > 5 for n in counts]

print(list(compress(addresses, more5)))
