#!/usr/bin/env python3
"""UDP Sleep Server"""

from socket import *
from time import ctime, sleep


HOST = ''
PORT = 32145
BUFSIZ = 1024
ADDR = (HOST, PORT)
MAXTIME = 60    # Minutes

with socket(AF_INET, SOCK_DGRAM) as udpSerSock:
    udpSerSock.bind(ADDR)
    print("Whiting for request...")
    while True:
        # Wait for an request
        data, addr = udpSerSock.recvfrom(BUFSIZ)
        timedata = data.decode('utf-8')
        # Check whether the data is an integer number and
        # it not exceeds the max rate
        if not timedata.isdigit() or int(timedata) > MAXTIME:
            udpSerSock.sendto(b"", addr)
        # Start timer for the number of minutes
        else:
            timedata = int(timedata) * 60
            print("Timer has been started for the address", addr)
            sleep(timedata)
            print("Timer is finished for the address", addr)
            udpSerSock.sendto(b"Wake up, Neo.", addr)
