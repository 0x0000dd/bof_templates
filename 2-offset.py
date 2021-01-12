#!/usr/bin/python

import socket

rhost = "0.0.0.0"
rport = 1234

pattern = ""

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((rhost,rport))
print "Sending: %s" % str(len(pattern))
s.send(pattern)
s.close()
