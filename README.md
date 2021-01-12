<h2>Description</h2>

Windows x86 Buffer Overflow Templates for OSCP

<h2>Steps</h2>

1. start service/app & start immunity as admin
1. fuzz input to determine overflow
1. generate pattern with `msf-pattern_create -l <LEN>`
