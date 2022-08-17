import threading

import xlrd
from utils.Tower import Tower


def parseExcel(xls):
    xls = xlrd.open_workbook(xls)
    towers = dict()
    sheets = xls.sheets()
    for sheet in sheets:
        tower = Tower(sheet)
        towers[sheet.name] = tower
    return towers


class TowerModel:
    def __init__(self, xls):
        self.towers = parseExcel(xls)
        pass

    # 执行某个tower模型
    def run(self):
        for name in self.towers:
            self.towers[name].start()

    def stop(self):
        for name in self.towers:
            self.towers[name].stop()