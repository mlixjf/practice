class A(object):

    def func(self):
        print("A.func")


class B(A):
# class B(object):

    def func(self):
        # super(B, self).func()
        print("B.func")


class C(A):
# class C(object):
    def func(self):
        # super(C, self).func()
        print("C.func")


class E(B, C):
    def func(self):
        super(E, self).func()
        print("E.func")


if __name__ == '__main__':
    e = E()
    e.func()
    print(E.__mro__)
    super(E, E()).func()

    data = {"name": 123}
    data.update({"age": 23})
    print(data)

    data = {'month': None, 'weekday': None, 'day': None, 'hour': None, 'minute': 0, 'second': 0, 'time_str': '2022-01-01 10:00:00', 'comments': '只有这1个触发时间'}
    data.update({'start': '2021-06-16 09:00:00', 'end': '2021-06-16 10:00:00'})
    print(data)