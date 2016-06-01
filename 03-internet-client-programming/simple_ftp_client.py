#!/usr/bin/env python3
import ftplib
import os
import socket


HOST = 'ftp.mozilla.org'
DIRN = 'pub/webtools'
FILE = 'bugzilla-LATEST.tar.gz'

def main():
    try:
        f = ftplib.FTP(HOST)
    except (socket.error, socket.gaierror) as e:
        print('ERROR: cannot reach "{}"'.format(HOST))
        return
    print('*** Connected to host "{}"'.format(HOST))

    try:
        f.login()
    except ftplib.error_perm:
        print('ERROR: cannot login anonymously')
        f.quit()
        return
    print('*** Logged in as anonymous')

    try:
        f.cwd(DIRN)
    except ftplib.error_perm:
        print('ERROR: cannot CD to "{}"'.format(DIRN))
        f.quit()
        return
    print('*** Changed to "{}" folder'.format(DIRN))

    try:
        f.retrbinary('RETR {}'.format(FILE), open(FILE, 'wb').write)
    except ftplib.error_perm:
        print('ERROR: cannot read file "{}"'.format(FILE))
        os.unlink(FILE)

    else:
        print('*** Downloaded "{}" to CWD'.format(FILE))
        f.quit()


if __name__ == '__main__':
    main()
