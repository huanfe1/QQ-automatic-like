# _*_ coding:utf-8 _*_

import os
import time
import webbrowser
import winreg

import psutil
import win32api
import win32con
import win32gui


def get_hwnd(name='的资料'):
    """返回标题中含有name的窗口句柄"""
    hwnd_title = {}
    hwnds = []

    def get_all_hwnd(hwnd, _):
        if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
            hwnd_title.update({win32gui.GetWindowText(hwnd): hwnd})
        for title, hwnd in hwnd_title.items():
            if name in title and hwnd not in hwnds:
                hwnds.append(hwnd)

    win32gui.EnumWindows(get_all_hwnd, 0)
    return hwnds


def on_click(hwnd):
    """点击QQ名片赞按钮"""
    like_position = win32api.MAKELONG(330, 340)
    close_position = win32api.MAKELONG(710, 20)
    for _ in range(11):
        # 点11次赞,防止漏点
        win32api.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, like_position)
        win32api.SendMessage(hwnd, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, like_position)
        time.sleep(0.3)
    # 点击关闭按钮
    win32api.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, close_position)
    win32api.SendMessage(hwnd, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, close_position)


def check_process():
    """检测QQ进程是否存在,不存在则尝试启动"""
    names = [psutil.Process(pid).name() for pid in psutil.pids()]
    if 'QQ.exe' not in names:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r'SOFTWARE\WOW6432Node\Tencent\QQ2009')
        qq_file = winreg.QueryValueEx(key, 'Install')[0] + r'\Bin\QQ.exe'
        os.startfile(qq_file)
        print('检测到QQ程序未存在,正在尝试启动')


if __name__ == '__main__':
    with open('qq.txt', 'r') as file:
        qq_numbers = file.read().split('\n')
    while qq_numbers:
        for i in range(10):
            qq_number = qq_numbers.pop()
            print(qq_number)
            webbrowser.open(f"tencent://ContactInfo/?subcmd=ViewInfo&puin=0&uin={qq_number}")
            time.sleep(0.2)
        # 运行两次,防止第一次打开时没有获取到句柄
        for _ in range(2):
            for i in get_hwnd():
                on_click(i)
