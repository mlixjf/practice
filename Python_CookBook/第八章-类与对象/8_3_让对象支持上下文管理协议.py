from socket import AF_INET, SOCK_STREAM, socket
from typing import Tuple


class LazyConnection(object):

    def __init__(self, address: Tuple[str, int],
                 family: int = AF_INET,
                 type_: int = SOCK_STREAM):
        self.address = address
        self.family = family
        self.type_ = type_
        self.connections = []

    def __enter__(self):
        sock = socket(self.family, self.type_)
        sock.connect(self.address)
        self.connections.append(sock)
        return sock

    def __exit__(self, exc_type, exc_value):
        self.connections.pop().close()


if __name__ == '__main__':
    conn = LazyConnection(("127.0.0.1", 8081))

    with conn as s1:
        pass
        with conn as s2:
            pass
