import socket

HOST = "localhost"
POST = 8080
BUFFER = 1024
ADDRESS = (HOST, POST)

while True:
    client_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_server.connect(ADDRESS)

    data = input(">")
    if not data:
        break
    client_server.send(data.encode("utf-8"))
    msg = client_server.recv(BUFFER)
    print(msg.decode("utf-8"))
    if not data:
        break
    client_server.close()