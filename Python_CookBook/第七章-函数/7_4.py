def my_fun():
    return 1, 2, 3


if __name__ == '__main__':
    a, b, c = my_fun()
    x = my_fun()

    y = 1, 2
    z = (1, 2)
    print(y, z)
