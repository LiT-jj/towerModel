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


def main():
    global model
    model.start()


if __name__ == '__main__':
    # 监听线程
    listener = keyboard.Listener(on_press=on_press)
    listener.start()

    xls = r'tower/logout.xls'
    model = TowerModel(xls=xls)
    model.run()

