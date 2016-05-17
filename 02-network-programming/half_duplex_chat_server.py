#!/usr/bin/env python3
"""TCP Half-Duplex Chat Server Client"""

from socket import *
from time import ctime


HOST = ""
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)
INDT = 25       # Indentation for messages alignment

with socket(AF_INET, SOCK_STREAM) as chat_server:
    chat_server.bind(ADDR)
    chat_server.listen(1)
    while True:
        print("Waiting for connections...")
        conn, addr = chat_server.accept()
        with conn:
            print("[{0}]".format(ctime()), "Connection is made with", addr)
            while True:
                client_data = conn.recv(BUFSIZ)
                if not client_data: break
                print("{0:<{indt}}{1}".format("Client message:",
                                              client_data.decode(),
                                              indt=INDT))
                server_data = input("{0:<{indt}}".format("Enter server message:",
                                                         indt=INDT))
                if not server_data: break
                conn.sendall(bytes(server_data, 'utf-8'))
            print("[{0}]".format(ctime()), "Connection is closed with", addr)
