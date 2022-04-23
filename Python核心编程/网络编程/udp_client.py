import socket

HOST = "127.0.0.1"
POST = 55555
ADDRESS = (HOST, POST)
BUFFER = 1024

udp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    data = input(">")
    if not data:
        break
    udp_client_socket.sendto(data.encode("utf-8"), ADDRESS)
    data, add = udp_client_socket.recvfrom(BUFFER)
    print(data.decode("utf-8"), add)