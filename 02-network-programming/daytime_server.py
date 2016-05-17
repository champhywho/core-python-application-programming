#!/usr/bin/env python3
"""UDP Daytime Server"""

from socket import *
from time import ctime


SERVICE = 'daytime'
PROTOCOL = 'udp'
PORT = getservbyname(SERVICE, PROTOCOL)
HOST = ''
BUFSIZ = 0
ADDR = (HOST, PORT)

with socket(AF_INET, SOCK_DGRAM) as udpSerSock:
    udpSerSock.bind(ADDR)
    print("Daytime server is waiting for request...")
    while True:
        data, addr = udpSerSock.recvfrom(BUFSIZ)
        udpSerSock.sendto(bytes(ctime(), 'utf-8'), addr)
        print("Request is received from and returned to:", addr)
