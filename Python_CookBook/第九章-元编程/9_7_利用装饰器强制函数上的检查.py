import inspect
from datetime import datetime
from functools import wraps


def typeassert(*ty_type, **ty_kwargs):

    def decorate(func):
        signature = inspect.signature(func)
        bounds_type = signature.bind_partial(*ty_type, **ty_kwargs).arguments

        @wraps(func)
        def wrapper(*args, **kwargs):
            bound_values = signature.bind(*args, **kwargs).arguments
            for name, value in bound_values.items():
                if name in bounds_type:
                    if not isinstance(value, bounds_type[name]):
                        raise TypeError(f"{func.__name__}函数的{name}参数值应为{bounds_type[name]}类型")
            return func(*args, **kwargs)
        return wrapper
    return decorate


@typeassert(int, y=int)
def add(x: int, y: int, z: int):
    return x + y + z


# signature = inspect.signature(add)
# print(signature)
# print(signature.parameters)
# print(signature.parameters["x"].name)
# print(signature.parameters["x"].kind)
#
# bounds_type = signature.bind_partial(int, z=int)
# print(bounds_type.arguments)
# print(signature.bind(1, 2, 3))

if __name__ == '__main__':
    # add(1, 2.0, 2.0)
    # add(1.0, 2, 2)

    t = datetime.now()
    print(t.timestamp())