#!/usr/bin/env python
# -*- coding:utf8 -*-

import socket
import os
import sys

HOST = "218.150.183.48"
PORT = 8012
ADDR = (HOST, PORT)
BUFSIZE = 4096

videofile = "/home/pi/Documents/Final/Photo.jpg"
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
filename = "Photo.jpg"

serv.listen(5)
conn, addr = serv.accept()
print 'client connected ...', addr


f= open(filename,'rb')  #open Read Binary
data=f.read()
print data,',,,'

exx=conn.sendall(data)
print exx,'...'
f.flush()
f.close()


print'finished writing file'

conn.close()
serv.close()