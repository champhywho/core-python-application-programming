#!/usr/bin/env python3

from random import randrange, choice
from string import ascii_lowercase as lc
from sys import maxsize
from time import ctime


tlds = ('com', 'edu', 'net', 'org', 'gov')

with open(r'redata.txt', 'a') as f:
    for i in range(randrange(5, 11)):
        dtint = randrange(maxsize)
        dtstr = ctime(dtint)
        llen = randrange(4, 8)
        login = ''.join(choice(lc) for j in range(llen))
        dlen = randrange(llen, 13)
        dom = ''.join(choice(lc) for j in range(dlen))
        line = "{0}::{1}@{2}.{3}::{4}-{5}-{6}\n".format(
                dtstr, login, dom, choice(tlds), dtint, llen, dlen)
        f.write(line)
