# -*- coding: UTF-8 -*-
#!/usr/bin/env python3
import socket


def create_server(hello_string):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = 12345
    # 0.0.0.0 means expose it to all of the IPs alotted to our device
    # on all connected networks
    server_socket.bind(('0.0.0.0', port))
    # Accept maximum 5 connections at a time
    server_socket.listen(5)
    # Keep the server running forever
    print('Server running at port', port)
    while True:
        # Accept the connection if a client tries to connect
        connection = server_socket.accept()
        print('Accepted Connection',connection)
        # Each connection has two things first the socket stream and the second the address
        conn, addr = connection
        print('Connection from', addr)
        # Send hello_string bytes to client
        conn.send(hello_string)
        # Close the connection with that client
        conn.close()


def main():
    create_server(b'Hello from the server')


if __name__ == "__main__":
    main()
