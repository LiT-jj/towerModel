# -*- coding: utf-8 -*-
import pyautogui as pag
import time

import win32gui


def clicks_img(img_path, duration=0.2, confidence=0.9):
    box = pag.locateOnScreen(img_path, confidence=confidence)
    pag.moveTo(box, duration=duration)
    pag.doubleClick(box)


def contains_img(img_path, confidence=0.8):
    box = pag.locateOnScreen(img_path, confidence=confidence)
    if box is not None:
        return True
    else:
        return False


def write(content, win=None, duration=0.2):
    [pos, info] = content.split(' ')
    [x, y] = pos.split(',')
    pag.moveTo(int(x) + win[0], int(y) + win[1], duration=duration)
    pag.click()
    pag.hotkey('ctrl', 'a')
    pag.press('backspace')
    pag.write(info)
    pag.press('enter')


def doWhile(content, duration=0.2):
    pass


def doWhileUtilContainImage(content, duration=0.2):
    while True:
        if contains_img(content):
            print("找到图片, 退出循环...")
        else:
            time.sleep(duration)


def doIf(content):
    [conditions, TNS, FNS] = content.split(' ')
    conditions = conditions.split('+')
    flag = True
    for condition in conditions:
        flag = doCondition(condition) and flag
        if not flag:
            break
    return TNS if flag else FNS


def doCondition(condition):
    t, c = condition.split('-')
    if t == 'image':
        return contains_img(c)
    return False


def setWin(content):
    hWnd = win32gui.FindWindow(None, content)
    assert hWnd != 0, '找不到窗口: {0}...'.format(content)
    win32gui.SetForegroundWindow(hWnd)
    win32gui.SetActiveWindow(hWnd)
    win = win32gui.GetWindowRect(hWnd)
    return win


if __name__ == '__main__':
    doWhile(r'image C:\Users\LiT\Desktop\towerModel\img\loginPage.png')
