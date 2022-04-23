import socket
from datetime import datetime

HOST = "127.0.0.1"
PORT = 55555
ADDRESS = (HOST, PORT)
BUFFER = 1024

udb_server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udb_server_socket.bind(ADDRESS)

while True:
    print("waiting for connection")
    msg, add = udb_server_socket.recvfrom(BUFFER)
    print(msg, add)
    if not msg:
        break

    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S").encode("utf-8")
    split_symbol = ":".encode("utf-8")
    data = date + split_symbol + msg
    udb_server_socket.sendto(data, add)

udb_server_socket.close()