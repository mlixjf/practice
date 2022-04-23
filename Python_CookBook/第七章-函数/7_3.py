def add(x: int, y: int) -> int:
    """add"""
    return x + y


if __name__ == '__main__':
    print(help(add))
    print(add.__annotations__)
    print(dir(add))
object