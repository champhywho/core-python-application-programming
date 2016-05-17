#!/usr/bin/env python3
import socket
import os.path


BUFSIZ = 1024
TMPFILE = r"/tmp/python_unix_sockets_example"

print("Connecting...")
if os.path.exists(TMPFILE):
    with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as client:
        client.connect(TMPFILE)
        while True:
            data = input('\nEnter a command:\n')
            if not data: break
            client.send(bytes(data, 'utf-8'))

            data = client.recv(BUFSIZ)
            if not data: break
            print(data.decode('utf-8'))
else:
    print("Couldn't Connect!")
