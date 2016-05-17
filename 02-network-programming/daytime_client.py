#!/usr/bin/env python3
"""UDP Daytime Server Client"""

from socket import *


SERVICE = 'daytime'
PROTOCOL = 'udp'
PORT = getservbyname(SERVICE, PROTOCOL)
HOST = 'localhost'
BUFSIZ = 1024
ADDR = (HOST, PORT)

print("Press Enter key to get a current time.\nOr type 'exit' to leave.")
with socket(AF_INET, SOCK_DGRAM) as udpCliSock:
    while True:
        data = input()
        if data.lower() == 'exit': break
        udpCliSock.sendto(b'', ADDR)
        data, addr = udpCliSock.recvfrom(BUFSIZ)
        print(data.decode())
