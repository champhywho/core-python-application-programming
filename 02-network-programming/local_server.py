#!/usr/bin/env python3
import socket
import os, os.path
from time import ctime


BUFSIZ = 1024
TMPFILE = r"/tmp/python_unix_sockets_example"

if os.path.exists(TMPFILE):
    os.remove(TMPFILE)

print("Opening socket...")
with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as server:
    server.bind(TMPFILE)
    server.listen(1)
    print("Listening...")
    while True:
        conn, addr = server.accept()
        print("New connection accepted...")
        while True:
            data = conn.recv(BUFSIZ)
            if not data: break
            data = data.decode('utf-8')

            send_data = "Unknown command"

            if data == 'date':
                send_data = ctime()
            elif data == 'os':
                send_data = os.name
            elif data == 'ls':
                send_data = "\n".join(os.listdir())
            elif data.startswith('ls ') and len(data.split()) > 1:
                send_data = "\n".join(os.listdir(data.split()[1]))

            conn.send(bytes("\n--Response--\n{0}".format(send_data), 'utf-8'))
        print("...connection closed")
