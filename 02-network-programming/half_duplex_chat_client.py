#!/usr/bin/env python3
"""TCP Half-Duplex Chat Client"""

from socket import *


HOST = "localhost"
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)
INDT = 25

with socket(AF_INET, SOCK_STREAM) as chat_client:
    chat_client.connect(ADDR)
    while True:
        client_data = input("{0:<{indt}}".format("Enter your message:",
                                                 indt=INDT))
        if not client_data: break
        chat_client.sendall(bytes(client_data, 'utf-8'))
        server_data = chat_client.recv(BUFSIZ)
        if not server_data: break
        print("{0:<{indt}}{1}".format("Server message:",
                                      server_data.decode(),
                                      indt=INDT))
