from operator import itemgetter, attrgetter
rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

rows_by_fname = sorted(rows, key=itemgetter("fname"))
print(rows_by_fname)

rows_by_uid = sorted(rows, key=lambda row: row["uid"])
print(rows_by_uid)

print(min(rows, key=lambda row: row["uid"]))
print(min(rows, key=itemgetter("uid")))

print("name".split("."))