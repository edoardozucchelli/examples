import sys
import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)


def simple_socket():
    """ socket.socket() creates a socket object that supports the context manager type.
    The arguments passed to socket() specify the address family and socket type.
    AF_INET is the Internet address family for IPv4. SOCK_STREAM is the socket type
    for TCP, the protocol that will be used to transport our messages in the network. """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # bind() is used to associate the socket with a specific network interface and port number.
        s.bind((HOST, PORT))
        # listen() enables a server to accept() connections creating a listening socket.
        s.listen()
        # accept() blocks and waits for an incoming connection. When a client connects,
        # it returns a new socket object representing the connection and a tuple holding
        # the address of the client.The tuple will contain (host, port) for IPv4 connections.
        conn, addr = s.accept()
        # After getting the client socket object conn from accept(), an infinite while loop
        # is used to loop over blocking calls to conn.recv(). This reads whatever data the
        # client sends and echoes it back using conn.sendall().
        # If conn.recv() returns an empty bytes object, b'', then the client closed the
        # connection and the loop is terminated. The with statement is used with conn to
        # automatically close the socket at the end of the block.
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024)
                # if not data:
                #     break
                if data:
                    print(data)
                conn.sendall(data)


if __name__ == "__main__":
    args = sys.argv
    # args[0] = current file
    # args[1] = function name
    # args[2:] = function args : (*unpacked)
    globals()[args[1]](*args[2:])
