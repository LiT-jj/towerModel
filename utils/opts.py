# -*- coding: utf-8 -*-
import pyautogui as pag
import time


def clicks_img(img_path, duration=0.01):
    box = pag.locateOnScreen(img_path)
    pag.moveTo(box, duration=duration)
    pag.doubleClick(box)


def contains_img(img_path, confidence=0.8):
    box = pag.locateOnScreen(img_path, confidence=confidence)
    if box is not None:
        return True
    else:
        return False
