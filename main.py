import sys
import threading
import time

import pynput
from pynput import keyboard
from utils.TowerModel import TowerModel


def on_press(key):
    global model
    if not isinstance(key, pynput.keyboard._win32.KeyCode) and key.name == 'esc':
        model.stop()


if __name__ == '__main__':
    gloabl_parmeter = dict()
    # 监听线程
    listener = keyboard.Listener(on_press=on_press)
    listener.start()

    xls = r'bilibili.xls'
    model = TowerModel(xls=xls)
    model.run(name='我的关注界面', floor=1)

