from functools import partial

RECORD_SIZE = 32

with open("data/data.data", "wb") as f:
    f.write("12345678912345678912345678".encode("utf-8"))
    f.writelines(["12345678912345678912345678".encode("utf-8"),
                  "12345678912345678912345678".encode("utf-8"),
                  "12345678912345678912345678".encode("utf-8")])

with open("data/data.data", "rb") as f:
    records = iter(partial(f.read, RECORD_SIZE), "b")
    for record in records:
        if len(record) > 0:
            print(len(record))
            print(record.decode("utf-8"))
        else:
            break
