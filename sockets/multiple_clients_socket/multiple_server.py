import socket
import threading

HOST = '127.0.0.1'
PORT = 54321


def request_handler(conn, addr):
    with conn:
        print(conn, addr)

        while True:
            data = conn.recv(1024)
            print(data.decode('utf-8'))

            if not data:
                break

            conn.sendall(data)


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()

        while True:
            print('Ready to accept connection from client')

            conn, addr = s.accept()
            print('Connected with', addr[0], ':', str(addr[1]))

            t = threading.Thread(target=request_handler, args=(conn, addr), daemon=True)
            t.start()


if __name__ == '__main__':
    main()
