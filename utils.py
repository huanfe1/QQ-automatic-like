# _*_ coding:utf-8 _*_
# 输出鼠标在窗口内的坐标

import win32api
import win32gui
import time

windowRec = win32gui.GetWindowRect(1575248)  # 目标子句柄窗口的坐标

while True:
    tempt = win32api.GetCursorPos()  # 记录鼠标所处位置的坐标
    x = tempt[0] - windowRec[0]  # 计算相对x坐标
    y = tempt[1] - windowRec[1]  # 计算相对y坐标
    print(x, y)
    time.sleep(0.5)  # 每0.5s输出一次
