import xlrd
import time
import pyautogui as pag
from utils import opts

o2i = dict()

def initO2I(sheet):
    global o2i
    opt_info = sheet.row_values(rowx=0, start_colx=0, end_colx=None)
    o2i = dict()
    for idx, key in enumerate(opt_info):
        o2i[key] = idx

def parseRow(sheet, row):
    global o2i
    opt_info = sheet.row_values(rowx=row, start_colx=0, end_colx=None)
    type = opt_info[o2i['type']]
    step = opt_info[o2i['step']]
    comment = opt_info[o2i['comment']]
    wait_time = opt_info[o2i['wait_time']]
    img_path = opt_info[o2i['img_path']]
    content = opt_info[o2i['content']]
    print("步骤: {0}\t操作类型: {1}\t 功能描述:{2}".format(step, type, comment))
    if type == 'clicks image':
        opts.clicks_img(img_path)
    if type == 'contains image':
        res = opts.contains_img(img_path)
        assert res, '指定区域没有图片...'
    if type == 'window operation':
        windows = pag.getActiveWindow()
        content = int(content)
        for sub_row in range(row + 1, row + content + 1):
            parseRow(sheet, sub_row)
        row = row + content + 1
    time.sleep(wait_time)
    pass

def main():
    table = xlrd.open_workbook(r'tower/QQlogin.xlsx')
    sheet = table.sheets()[0]
    initO2I(sheet)
    for row in range(1, sheet.nrows):
        parseRow(sheet, row)


if __name__ == '__main__':
    main()