import psutil

def processinfo(processName):
    pids = psutil.pids()
    for pid in pids:
        p = psutil.Process(pid)
        if p.name() == processName:
        	return(pid)
