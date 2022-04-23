import inspect

import collections
import functools
import inspect


def para_check(func):
    """
    函数参数检查装饰器，需要配合函数注解表达式（Function Annotations）使用
    """
    msg = 'Argument {argument} must be {expected!r},but got {got!r},value {value!r}'

    # 获取函数定义的参数
    sig = inspect.signature(func)
    parameters = sig.parameters  # 参数有序字典
    arg_keys = tuple(parameters.keys())  # 参数名称
    print(dir(sig))

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        CheckItem = collections.namedtuple('CheckItem', ('anno', 'arg_name', 'value'))
        check_list = []

        # collect args   *args 传入的参数以及对应的函数参数注解
        for i, value in enumerate(args):
            arg_name = arg_keys[i]
            anno = parameters[arg_name].annotation
            check_list.append(CheckItem(anno, arg_name, value))

        # collect kwargs  **kwargs 传入的参数以及对应的函数参数注解
        for arg_name, value in kwargs.items():
            anno = parameters[arg_name].annotation
            check_list.append(CheckItem(anno, arg_name, value))

        # check type
        for item in check_list:
            if not isinstance(item.value, item.anno):
                error = msg.format(expected=item.anno, argument=item.arg_name,
                                   got=type(item.value), value=item.value)
                raise TypeError(error)

        return func(*args, **kwargs)

    return wrapper


def check_parameter(func):
    func_signature = inspect.signature(func)
    func_parameters = func_signature.parameters
    LocalParameter = collections.namedtuple(
        "LocalParameter", ["value", "name", "annotation"])
    check_list = ["forward_ms", "price"]

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = []

        # 位置参数
        result.extend([LocalParameter(arg, func_parameter.name, func_parameter.annotation)
                       for arg, func_parameter in zip(args, func_parameters.values())
                       if func_parameter.name in check_list])
        # 关键字参数
        result.extend([LocalParameter(value, key, func_parameters[key].annotation)
                       for key, value in kwargs.items()
                       if key in check_list])

        for p in result:
            if isinstance(p.value, p.annotation):
                continue
            else:
                raise TypeError(f"{func.__name__}函数的{p.name}参数值应为int类型")

        return func(*args, **kwargs)
    return wrapper


# @para_check
@check_parameter
def test(x: int, forward_ms: int, price: float):
    print(x, forward_ms, price)


if __name__ == '__main__':
    test(1, forward_ms=2, price=2.1)
