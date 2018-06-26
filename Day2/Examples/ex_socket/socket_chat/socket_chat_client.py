# -*- coding: UTF-8 -*-
#!/usr/bin/env python3
import socket


def create_client():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('', 12345))
    while True:
        choice = input('>>> Input recv to receive message send to send message > ')
        if choice == 'recv':
            print(s.recv(2048))
        elif choice == 'send':
            msg = input('>>> Enter your message > ')
            # It can only send bytes so we need to convert it to bytes
            s.send(bytes(msg, 'utf-8')) 


def main():
    create_client()


if __name__ == "__main__":
    main()
