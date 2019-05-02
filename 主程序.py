import psutil
import win32api



#检测QQPID如果不存在则启动
def processinfo(processName):
    pids = psutil.pids()
    for pid in pids:
        p = psutil.Process(pid)
        if p.name() == processName:
        	return(pid)
result = processinfo("QQ.exe")
if result == None:
	print("QQ程序不存在，正在尝试启动")
	win32api.ShellExecute(0, 'open', 'D:\\QQ\\Bin\\QQ.exe', '','',1)
else:
	print("QQ程序已存在")
