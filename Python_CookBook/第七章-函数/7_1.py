import html


def avg(first: int, *rest) -> float:
    """"""
    return (first + sum(rest)) / (len(rest) + 1)


def make_element(name, value, **attrs) -> str:
    keys = [" %s='%s'" % item for item in attrs.items()]
    attr_str = "".join(keys)
    element = "<{name}{attrs}>{value}</{name}>".format(
        name=name,
        attrs=attr_str,
        value=html.escape(value)
    )
    print(keys, attr_str, element, html.escape(value))
    return element


def any_args(*args, **kwargs):
    print(f"args:{args} type:{type(args)}")
    print(f"kwargs:{kwargs} type:{type(kwargs)}")


def a(x, *args, y):
    print(locals())


def b(x, *args, y, **kwargs):
    print(locals())


if __name__ == '__main__':
    print(avg(1, 2, 3))
    any_args(1, 2, 3, name="xiaoming", age=18)
    a(1, 2, y=3)
    b(1, 2, y=3, z=4)
    print(make_element('item', 'Albatross', size='large', quantity=6))
    print(make_element("p", "<spam>"))
    print("%s=%s" % ("name", "test"))