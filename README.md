# oneproc
A light-weight Python class that uses a pid file to determine if the application is already running. It defaults to a pid file in the same folder as the program that launched it.

## Example
```python
import sys
from oneproc import OneProc

myproc = OneProc()
if not myproc.lock_pid():
    print(myproc.errmsg)
    sys.exit(1)
else:
    print("Got the lock:", myprod.pid)
    # Do stuff...
