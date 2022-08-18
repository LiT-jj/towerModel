# -*- coding: utf-8 -*-
import pyautogui as pag
import time

import win32gui


def click_img(img_path, duration=0.2, confidence=0.9, clickType=None):

    box = pag.locateOnScreen(img_path, confidence=confidence)
    assert box is not None, '找不到图片: {0}'.format(img_path)
    pag.moveTo(box, duration=duration)
    if clickType is None:
        pag.click()
    elif clickType == 'double':
        pag.doubleClick(box)
    elif clickType == 'right':
        pag.rightClick(box[0] + box[2], box[1])


def click(content):
    clickType, clickTime = content.split(' ')
    if clickType == 'left':
        if time == '1':
            pag.click()
        else:
            pag.doubleClick()
    elif clickType == 'right':
        pag.rightClick()

def press(content):
    pag.press(content)

def contain_img(img_path, confidence=0.8):
    box = pag.locateOnScreen(img_path, confidence=confidence)
    if box is not None:
        return True
    else:
        return False


def write(content, duration=0.2):
    pag.hotkey('ctrl', 'a')
    pag.press('backspace')
    pag.write(formatUnit(content), interval=0.1)

def formatUnit(content):
    if isinstance(content, float):
        (_, num) = str(content).split('.')
        if num == '0':
            return str(int(content))
    return content

def moveTo(content, win=None, duration=0.2):
    checkType, info = content.split(' ')
    if checkType == 'image':
        img_path, confidence = info.split(',')
        box = pag.locateCenterOnScreen(img_path, confidence=confidence)
        assert box is not None, 'opts.py function: moveTo info: 找不到指定图片{0}'.format(img_path)
        pag.moveTo(box, duration=0.2)

def moveBy(content, win=None, duration=0.2):
    checkType, info = content.split(' ')
    if checkType == 'pos':
        x, y = info.split(',')
        pag.move(int(x), int(y), duration=0.2)

def doWhile(content, duration=0.2):
    pass


def doWhileUtilContainImage(content, duration=0.2):
    while True:
        if contain_img(content):
            print("找到图片, 退出循环...")
        else:
            time.sleep(duration)


def doIf(content):
    [conditions, TNS, FNS] = content.split(' ')
    conditions = conditions.split('+')
    for condition in conditions:
        flag = doCondition(condition)
        if not flag:
            return FNS
    return TNS


def doCondition(condition):
    t, c = condition.split('-')
    if t == 'image':
        img_path, confidence = c.split(',')
        return contain_img(img_path=img_path, confidence=confidence)
    return False


def setWin(content):
    t, c = content.split(' ')
    win = None
    if t == 'win_name':
        hWnd = win32gui.FindWindow(None, c)
        assert hWnd != 0, '找不到窗口: {0}...'.format(content)
        win32gui.SetForegroundWindow(hWnd)
        win32gui.SetActiveWindow(hWnd)
        win = win32gui.GetWindowRect(hWnd)
    if t == 'image':
        box = pag.locateOnScreen(c, confidence=0.9)
        assert box is not None, '找不到图片：{0}'.format(c)
        win = (int(box[0]), int(box[1]), int(box[0] + box[2]), int(box[1] + box[3]))
    return win
