#!/usr/bin/env python3
"""TCP Web Client"""

from socket import *


HOST = "devdreamer.me"
PORT = 80
BUFSIZ = 4096
ADDR = (HOST, PORT)
COMMND = "GET / HTTP/1.0\n\n"

with socket(AF_INET, SOCK_STREAM) as web_client:
    web_client.connect(ADDR)
    web_client.send(bytes(COMMND, 'utf-8'))
    with open('page.html', 'w') as page:
        while True:
            server_data = web_client.recv(BUFSIZ)
            if not server_data: break
            page.write(server_data.decode('utf-8'))
