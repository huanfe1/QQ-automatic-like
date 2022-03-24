import time
import webbrowser
import win32gui
import win32api
import win32con


# webbrowser.open("tencent://ContactInfo/?subcmd=ViewInfo&puin=0&uin=3036446123")


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
    # 点赞按钮位置
    like_position = win32api.MAKELONG(330, 340)
    # 关闭按钮位置
    close_position = win32api.MAKELONG(710, 20)
    for _ in range(11):
        # 点11次赞,防止漏点
        win32api.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, like_position)
        win32api.SendMessage(hwnd, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, like_position)
        time.sleep(0.1)
    # 点击关闭按钮
    win32api.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, close_position)
    win32api.SendMessage(hwnd, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, close_position)


for i in get_hwnd():
    on_click(i)
