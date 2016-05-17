#!/usr/bin/env python3
"""UDP Sleep Server Client"""

from socket import *


HOST = 'localhost'
PORT = 32145
BUFSIZ = 1024
ADDR = (HOST, PORT)

with socket(AF_INET, SOCK_DGRAM) as udpCliSock:
    while True:
        msg = """Enter a positive integer number (up to 60) of minutes to sleep
(or press Enter key to leave):
"""
        data = input(msg)
        # Stop if empty string
        if not data: break
        # Send otherwise
        udpCliSock.sendto(bytes(data, 'utf-8'), ADDR)
        # Wait for an answer
        answer, ADDR = udpCliSock.recvfrom(BUFSIZ)
        # If answer is empty then try to enter correct number again
        if not answer:
            continue
        # If it's not empty then print it and stop the loop
        else:
            print(answer.decode('utf-8'))
            break
