import threading
import socketserver


clients = {}


class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):

    global clients

    def handle(self):
        while True:

            cur_thread = threading.current_thread()

            if not clients.get(self.client_address[0]):
                clients[self.client_address] = cur_thread.name

            data = str(self.request.recv(1024), 'ascii')

            if not data:
                break

            response = bytes("{}: {}".format(cur_thread.name, data), 'ascii')
            self.request.sendall(response)


class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass


def main():
    server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)

    with server:
        ip, port = server.server_address

        print('Server:', ip, ':', port)

        server_thread = threading.Thread(target=server.serve_forever, daemon=True)

        server_thread.start()

        print("Server loop running in thread:", server_thread.name)

        server_thread.join()

        server.shutdown()


if __name__ == "__main__":
    HOST, PORT = '127.0.0.1', 54321
    main()
