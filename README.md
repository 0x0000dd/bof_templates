<h2>Description</h2>

Windows x86 Buffer Overflow Templates for OSCP

<h2>Steps</h2>

1. start service/app & start immunity as admin
1. fuzz input to determine overflow
1. generate pattern with `msf-pattern_create -l <LEN>`
1. get hex value of EIP
1. find exact offset with `msf-pattern_offset -l <LEN> -q <EIP>`
1. calculate buffer
1. find bad characters (ESP follow in dump)
1. search for modules with memory protections set to false & no bad chars in base address with `!mona modules`
1. if not all false, use `!mona jmp -r esp` & skip to step 12
1. determine op code of pointer with `msf-nasm_shell JMP ESP` (FFE4)
1. find pointer address with `!mona find -s "\xff\xe4" -m <MODULE>`
1. convert to little endian format
1. go to pointer address, hit F2 to set breakpoint
1. generate shellcode and run final exploit
