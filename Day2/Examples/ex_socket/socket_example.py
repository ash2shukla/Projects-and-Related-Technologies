# -*- coding: UTF-8 -*-
#!/usr/bin/env python3
import socket


def get_server_ip(website):
    host_ip = socket.gethostbyname(website)
    print('The IP Address of', website, 'is', host_ip)
    return host_ip


def test_socket_client(website):
    """ Tries to connect to website's servers
    """
    # AF_INET stands for IPv4 and SOCK_STREAM means TCP Protocol
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(s)
    host_ip = get_server_ip(website)
    s.connect((host_ip, 80))
    # laddr is localaddress ie. our address on the network (which is internet for this example)
    # raddr is remote address ie. google's server's address on the network
    print(s)
    # it means we have established a connection with google now


def main():
    # get_server_ip('www.google.com')
    test_socket_client('www.google.com')

if __name__ == "__main__":
    main()
