import time
from oneproc import OneProc

myproc = OneProc()
myproc.lock_pid()
if myproc.status:
    time.sleep(60)
