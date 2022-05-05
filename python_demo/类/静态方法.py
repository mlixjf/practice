class Demo:

    def func1(self):
        pass

    @classmethod
    def func2(cls):
        pass

    @staticmethod
    def func3():
        pass


if __name__ == '__main__':
    demo = Demo()
    print(demo)
    print(demo.func1)  # 与实例对象绑定
    print(demo.func2)  # 类方法与类绑定，对实例本身没关系
    print(demo.func3)  # 静态方法与类和实例都不是绑定的，可以理解为普通的的函数
