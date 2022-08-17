import threading

import xlrd
from utils.Tower import Tower


def parseExcel(xls, sheet=None):
    if sheet is None:
        xls = xlrd.open_workbook(xls)
        towers = dict()
        sheets = xls.sheets()
        for sheet in sheets:
            tower = Tower(sheet)
            towers[sheet.name] = tower
        return towers
    else:
        xls = xlrd.open_workbook(xls)
        towers = dict()
        sheet = xls.sheet_by_name(sheet)
        tower = Tower(sheet)
        towers[sheet.name] = tower
        return towers


class TowerModel:
    def __init__(self, xls):
        self.xls = xls
        self.towers = None
        pass

    # 执行某个tower模型
    def run(self, name=None):
        self.towers = parseExcel(xls=self.xls, sheet=name)
        if name is not None:
            self.towers[name].start()
        else:
            for name in self.towers:
                self.towers[name].start()

    def stop(self):
        for name in self.towers:
            self.towers[name].stop()
