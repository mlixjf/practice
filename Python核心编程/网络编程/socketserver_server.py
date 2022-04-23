from datetime import datetime
from socketserver import TCPServer, StreamRequestHandler

HOST = ""
PORT = 8080
ADDRESS = (HOST, PORT)


class TestRequestHandler(StreamRequestHandler):

    def handle(self) -> None:
        print("connected from:", self.client_address)
        date = datetime.now().strftime("%Y%m%d").encode("utf-8")
        split_flag = ":".encode("utf-8")
        data = date + split_flag + self.request.recv(1024)
        self.request.sendall(data)


tcp_server = TCPServer(ADDRESS, TestRequestHandler)

print("start server...")
tcp_server.serve_forever()
