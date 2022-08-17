from utils import opts
import pyautogui as pag
import time
import win32gui as wing
from utils.Floor import Floor


class Tower:
    def __init__(self, sheet):
        self.flag = True
        self.floors = None
        self.o2i = None
        self.global_parmeter = dict()
        self.parseSheet(sheet)

    def parseSheet(self, sheet):
        floors = dict()
        for row in range(sheet.nrows):
            record = sheet.row_values(rowx=row, start_colx=0, end_colx=None)
            if row == 0:
                # 解析出 o2i（字段对应的下标）
                o2i = dict()
                for idx, key in enumerate(record):
                    o2i[key] = idx
                self.o2i = o2i
            else:
                floor = Floor(record, self.o2i, self.global_parmeter)
                floors[row] = floor
        self.floors = floors

    def start(self):
        idx = 1
        win = None
        while idx <= len(self.floors) and self.flag:
            res = self.floors[idx].forward()
            if res is None:
                idx = idx + 1
            else:
                idx = int(res)

    def stop(self):
        self.flag = False
