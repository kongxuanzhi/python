#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

from PyQt5.QtWidgets import *

from clock.Buttons import *
from clock.Utils import center

# image: url(五角星.png);
style = '''
QPushButton#btn {
    background-color: #3c3f41;
    border-style: outset;
    border-width: 2px;
    border-radius: 10px;
    border-color: beige;
    font: bold 14px;
    min-width: 10em;
    padding: 6px;  
}

QPushButton#btn::hover {
    background-color: red;   
}
'''


class Test(QWidget):
    def __init__(self):
        super().__init__()
        self.init()
        self.setStyleSheet(style)

    def init(self):
        alert_lyt = QHBoxLayout()
        # btn = TextButton('test', '#3c3f41', '#ffffff', self)
        btn = QPushButton('fff', self)
        btn.setObjectName('btn')
        btn1 = QPushButton('fffs', self)
        btn1.setObjectName('btn')

        btn.setFixedSize(60, 60)
        alert_lyt.addWidget(btn)
        alert_lyt.addWidget(btn1)

        self.setLayout(alert_lyt)

        center(self)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    sp = Test()
    sys.exit(app.exec_())

# TODOLIST
# 1. 有可能的话，将LCD字体居中
# 2. 记录日志到xls
# 3. 自定义时间button
