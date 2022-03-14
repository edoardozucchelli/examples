import time
import socket


host = '127.0.0.1'
port = 54321


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))

        for i in range(1, 11):
            data = 'Sending Test info n. ' + str(i)

            time.sleep(2)

            if not data:
                break

            s.send(str.encode(data))

            res = s.recv(1024)
            print('Server Response:', res.decode('utf-8'))


if __name__ == '__main__':
    main()
