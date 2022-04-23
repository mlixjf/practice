"""
python的导入机制在导入模块的时候，会从sys.modules中进行查找，如果查找到该模块，则直接返回，
如果没有会根据sys.meta_path中的三个加载器，依次加载内建模块，冻结模块，最后根据sys.path的路径查找第三方模块。
因此一个模块内的对象只会被导入一次，这就是单例的一种实现方式。
"""


class Singleton(object):

    def __init__(self):
        self.name = "singleton"


singleton = Singleton()


def _test():
    print("该函数不会被模块导入")
