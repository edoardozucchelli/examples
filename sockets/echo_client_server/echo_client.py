import sys
import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432        # The port used by the server


def simple_client():
    """ The client creates a socket object, uses .connect() to connect to the server and calls s.sendall()
    to send its message. Lastly, it calls s.recv() to read the server’s reply and then prints it."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(b"Hello, world")
        data = s.recv(1024)

    print(f"Received {data!r}")


if __name__ == "__main__":
    args = sys.argv
    # args[0] = current file
    # args[1] = function name
    # args[2:] = function args : (*unpacked)
    globals()[args[1]](*args[2:])
