from utils import opts
import time


class Floor:
    def __init__(self, record, o2i, global_parmeter):
        self.step = None
        self.type = None
        self.comment = None
        self.wait_time = None
        self.content = None

        self.o2i = o2i
        self.global_parmeter = global_parmeter
        self.parse_record(record)

    def run(self):
        pass

    def parse_record(self, record):
        o2i = self.o2i
        self.step = record[o2i['step']]
        self.type = record[o2i['type']]
        self.comment = record[o2i['comment']]
        self.wait_time = record[o2i['wait_time']]
        self.content = record[o2i['content']]

    def forward(self):
        self.log()
        res = None
        if self.type == 'click image':
            opts.click_img(self.content, clickType='double')
        if self.type == 'set win':
            win = opts.setWin(content=self.content)
            self.global_parmeter['win'] = win
        if self.type == 'reset win':
            self.global_parmeter['win'] = None
        if self.type == 'input':
            opts.write(self.content, win=self.global_parmeter['win'])
        if self.type == 'while_util_contain_image':
            opts.doWhileUtilContainImage(self.content)
        if self.type == 'if':
            res = opts.doIf(self.content)
        if self.type == 'print':
            print(self.content)
        if self.type == 'right click image':
            opts.click_img(self.content, clickType='right')
        if self.type == 'click pos':
            opts.click(self.content, win=self.global_parmeter['win'])
        time.sleep(self.wait_time)
        return res

    def log(self):
        print("步骤: {0}\t操作类型: {1}\t 功能描述:{2}".format(self.step, self.type, self.comment))