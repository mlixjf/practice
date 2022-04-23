def recv(maxsize, *args, block):
    """Receive a message"""
    pass


def mininum(*values, clip=None):
    m = min(values)
    if clip is not None:
        m = clip if clip > m else m
    return m


if __name__ == '__main__':
    # recv(1024, True)
    recv(1024, block=True)
    print(mininum(1, 2, 3, 4, 5, clip=-1))