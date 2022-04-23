class Test:

    def __init__(self):
        print("init...")

    def __call__(self):
        print("call...")


if __name__ == '__main__':
    t = Test()
    # t()

    Student = type("Student", (object,), {"level": "high"})
    s = Student()
    print(dir(s))