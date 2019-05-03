import psutil
import win32api,win32gui,win32con
import time
import keyboard
import linecache
from 检测QQ程序 import processinfo
import re


#检测QQ程序是否存在
QQlife = processinfo("QQ.exe")
if QQlife == None:
	print("QQ程序不存在，正在尝试启动")
	win32api.ShellExecute(0, 'open', 'D:\\QQ\\Bin\\QQ.exe', '','',1)#此处为QQ程序路径
else:
	print("QQ程序已存在")

#判断QQ号行数
QQlines = len(open("QQ.txt", 'r').readlines())



#按Q提示
print("按下Q键开始点赞")
keyboard.wait(hotkey='q')
print("开始点赞")


i=1
for i in range(i,i+3):
	QQone = linecache.getline("QQ.txt",i)
	win32api.ShellExecute(0, 'open', 'tencent://ContactInfo/?subcmd=ViewInfo&puin=0&uin='+QQone, '','',1)
	print(i)

	