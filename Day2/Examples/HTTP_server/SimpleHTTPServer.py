# -*- coding: UTF-8 -*-
#!/usr/bin/env python3
import socket

def get_response(request):
    print(request)
    return 'HTTP/1.1 200 OK\r\nContent-Length: 10\r\n\r\nHello HTTP\r\n\r\n'.encode()


def runserver():
    HOST, PORT = '', 8888
    http_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    http_socket.bind((HOST, PORT))
    http_socket.listen(1)
    print('Listening at port',PORT)
    while True:
        conn, addr = http_socket.accept()
        print('Connected client', addr)
        request = conn.recv(1024)
        conn.send(get_response(request))


def main():
    runserver()
if __name__ == "__main__":
    main()
