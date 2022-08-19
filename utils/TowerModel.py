import threading

import xlrd
from utils.Tower import Tower


def parseExcel(xls, sheet=None):
    if sheet is None:
        xls = xlrd.open_workbook(xls)
        towers = dict()
        sheets = xls.sheets()
        for sheet in sheets:
            names = sheet.name.split('の')
            tower = Tower(sheet)
            if len(names) > 1:
                towers[names[0]].addSubTower(tower)
            else:
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
        self.towers = parseExcel(xls=self.xls)
        pass

    # 执行某个tower模型
    def run(self, name=None, floor=1):
        if name is not None:
            self.towers[name].start(floor)
        else:
            for name in self.towers:
                self.towers[name].start()

    def stop(self):
        for name in self.towers:
            self.towers[name].stop()
