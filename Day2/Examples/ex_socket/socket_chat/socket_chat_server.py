# -*- coding: UTF-8 -*-
#!/usr/bin/env python3

# As we need to continuously receive from each client and perform corresponding actions
# So we need to listen to each client in a thread

from threading import Thread
import socket

# store the client connections
client_list = []

class ClientThread(Thread):
    def __init__(self, client_conn, client_addr):
        Thread.__init__(self)
        self.conn = client_conn
        self.addr = client_addr

    def run(self):
        self.conn.send(b'Welcome to the chat')
        while True:
            message = self.conn.recv(2048)
            if message != b'':
                print(self.addr, 'sent', message)
                # receive message from client
                # send the message to all connected clients
                for client in client_list:
                    if client != self.conn:
                        client.send(message)


def create_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('', 12345))
    server_socket.listen(100)
    while True:
        conn, addr = server_socket.accept()
        print('Client connected', addr)
        client_list.append(conn)
        ClientThread(conn, addr).start()


def main():
    create_server()


if __name__ == "__main__":
    main()
