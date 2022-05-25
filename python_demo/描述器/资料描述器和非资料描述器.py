class M:
    """资料描述器"""

    def __init__(self):
        self.m = 1

    def __get__(self, instance, cls):
        print("M的get方法执行")
        return self.m

    def __set__(self, instance, value):
        print("M的set方法执行")
        self.m = value


class N:
    """非资料描述器"""

    def __init__(self):
        self.n = 2

    def __get__(self, instance, cls):
        print("N的get方法执行")
        return self.n


class Test(object):
    m = M()
    n = N()

    def __init__(self, m, n):
        self.m = m  # 在进行赋值时发现Test有类属性m，并且是一个资料描述器，调用描述器的__set__方法
        self.n = n


"""
def __getattribute__(self, key):
    v = object.__getattribute__(key)
    if hasattr(v, "__get__"):
        return v.__get__(self, type(self))
    return v
    """

if __name__ == '__main__':
    t = Test(1, 2)
    print(t.n)  # 2
    print(t.m)  # 1

    print(t.__dict__)
