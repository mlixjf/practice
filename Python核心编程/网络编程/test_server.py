from socket import socket, AF_INET, SOCK_STREAM, AF_INET6
from datetime import datetime
from time import ctime

HOST = ""
PORT = 5555
ADDRESS = (HOST, PORT)
BUFFER = 1024

ss = socket(AF_INET6, SOCK_STREAM)
ss.bind(ADDRESS)
ss.listen()

while True:
    print("wait for connection...")
    client_socket, address = ss.accept()
    print("connected from:", address)
    while True:
        data = client_socket.recv(BUFFER)
        if not data:
            break
        data = str(datetime.now()).encode("utf-8") + ":".encode("utf-8") + data
        client_socket.send(data)
    client_socket.close()

ss.close()