
import os
import sys
from pathlib import Path
import psutil
import time

class OneProc:
    def __init__(self, pid_file=''):
        self.pid = os.getpid()
        if pid_file=='':
            prog_path = Path(os.path.abspath(sys.argv[0])) 
            pid_file = prog_path.with_suffix('.pid')
        self.pid_file = pid_file
        self.apid = -1
        self.status = False

    def update_pid_file(self):
        try:
            with open(self.pid_file, 'w+') as pfile:
                pfile.write(str(self.pid))
                self.status = True
                return self.status
        except:
            self.errmsg = "ERROR opening pid_file:" + self.pid_file
            self.status = False
            return self.status
        
    def lock_pid(self):
        try:
            with open(self.pid_file, 'r') as pfile:
                apid = int(pfile.readline())
                self.alt_pid = apid
                if (self.pid != apid):
                    try:
                        process = psutil.Process(apid)
                        self.errmsg = "WARNING: Already running on PID:" + format(apid)
                        self.status = False
                    except psutil.NoSuchProcess:
                        return self.update_pid_file()
                    except Exception as e:
                        self.errmsg = "WARNING:" + str(e)
                        return self.update_pid_file()
                    self.status = False
                    return self.status
                else:
                    Path(self.pid_file).touch()
                    self.status = Trus
                    return self.status
        except Exception as e:
            self.errmsg = "WARNING: Issue opening pid file:" + self.pid_file + str(e)
            return self.update_pid_file()

if __name__ == '__main__':
    print("Testing OneProc")
    myproc = OneProc()
    print("pid", myproc.pid)
    print("status", myproc.lock_pid())
    if myproc.status:
        time.sleep(120)
    else:
        print("alt_pid", myproc.alt_pid)
        print("errmsg", myproc.errmsg)
    
