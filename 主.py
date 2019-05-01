import psutil
import win32api


#检测QQ进程是否存在
def judgeprocess(processname):
    pl = psutil.pids()
    for pid in pl:
        if psutil.Process(pid).name() == processname:
            break
    else:
        win32api.ShellExecute(0, 'open', 'D:\QQ\Bin\QQ.exe', '','',1)
        
if judgeprocess('QQ.exe') == 0:
    print('success')
else:
    pass


#打开QQ名片
win32api.ShellExecute(0, 'open', 'tencent://ContactInfo/?subcmd=ViewInfo&puin=0&uin=', '','',1)
