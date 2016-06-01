#!/usr/bin/env python3
from socket import *


HOST = "localhost"
PORT = 34512
BUFSIZ = 1024
ADDR = (HOST, PORT)

with socket(AF_INET, SOCK_STREAM) as name_client:
    name_client.connect(ADDR)
    while True:
        client_data = input("What type of service are you seeking?\n")
        if not client_data: break
        name_client.sendall(bytes(client_data, 'utf-8'))
        server_data = name_client.recv(BUFSIZ)
        if not server_data: break
        print('>>>', server_data.decode())
