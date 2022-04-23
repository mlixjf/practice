from socket import socket, AF_INET, SOCK_STREAM, AF_INET6

HOST = "localhost"
PORT = 5555
BUFFER = 1024
ADDRESS = (HOST, PORT)

cs = socket(AF_INET6, SOCK_STREAM)
cs.connect(ADDRESS)

while True:
    data = input("> ")
    if not data:
        break
    cs.send(data.encode("utf-8"))
    data = cs.recv(1024)
    if not data:
        break
    print(data.decode("utf-8"))

cs.close()