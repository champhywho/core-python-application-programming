#!/usr/bin/env python3
"""
Name server is responsible for maintaining a database of
hostname-port number pairs and returning them by clients requests.
"""

from socket import *


# A simple database of registered services
REGSRV = [['devdreamer.me', 80, 'My blog'],
          ['www.amazon.com', 80, 'Online shop'],
          ['www.google.com.ua', 80, 'Search engine']]

HOST = ""
PORT = 34512
BUFSIZ = 1024
ADDR = (HOST, PORT)

with socket(AF_INET, SOCK_STREAM) as name_server:
    name_server.bind(ADDR)
    name_server.listen(1)

    print("Waiting for connections...")
    while True:
        conn, addr = name_server.accept()
        print("Have a connection with", addr)
        with conn:
            while True:
                request_data = conn.recv(BUFSIZ).decode('utf-8').strip().lower()
                if not request_data:
                    break
                else:
                    for service in REGSRV:
                        if request_data in service[2].lower():
                            resp_data = "{0}:{1}".format(service[0],
                                                             service[1])
                            break
                    else:
                        resp_data = "Can't find such a service unfortunately..."
                conn.sendall(bytes(resp_data, 'utf-8'))
        print("Lost the connection with", addr)
