#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import (QWidget, QGridLayout, QVBoxLayout, QFrame,QLabel,
                             QHBoxLayout, QPushButton, QApplication, QLCDNumber
                             , QDesktopWidget)
from PyQt5.QtGui import QPainter, QFont, QColor, QPen, QIcon, QImage, QBrush, QCursor
from PyQt5.QtCore import Qt, QBasicTimer, QSize, QRect, QPoint
from Utils import center
from Buttons import ImageButton


style = '''
QPushButton#num-btn {
    background-color: #3c3f41;
    color: #ffffff;
    border-style: outset;
    border-width: 2px;
    border-radius: 10px;
    border-color: beige;
    font: bold 14px;
    min-width: 2em;
    padding: 6px;  
}

QPushButton#num-btn::hover {
    background-color: red;   
}
'''

class Dash(QWidget):
    def __init__(self, time, parent_board):
        super().__init__()
        self.setFixedSize(100, 60)
        self.lcd = QLCDNumber(self)
        # self.status_btn = QPushButton(QIcon('play_fill.png'), '', self)
        # self.status_btn = ImageButton('pause', , 'play_fill.png', self)
        self.status_btn = ImageButton('stop.png', 'play_fill.png', 'test', self)
        self.status_btn.setSize(QSize(25, 25))

        self.timer = QBasicTimer()
        self.time = time
        self.isPause = False
        self.parentBoard = parent_board
        self.init()

    def init(self):
        main_layout = QHBoxLayout(self)
        self.status_btn.connect(self.changeStatus)

        # self.status_btn.clicked.connect(self.changeStatus)
        main_layout.addWidget(self.status_btn)
        main_layout.addWidget(self.lcd, Qt.AlignCenter)
        self.timer.start(1000, self)

        self.move(2000, 2000)
        self.setStyleSheet("QWidget { background-color: #3c3f41 }")
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.show()

    def changeStatus(self):
        if self.isPause:
            self.timer.start(1000, self)
            self.isPause = False
            self.status_btn.setIcon(QIcon('play_fill.png'))
        else:
            self.timer.stop()
            self.isPause = True
            self.status_btn.setIcon(QIcon('stop.png'))

    def timerEvent(self, e):
        if self.time == 0:
            self.timer.stop()
            self.hide()
            self.parentBoard.show()
            return

        self.lcd.display(self.time)
        self.time = self.time - 1


class Sleep(QWidget):
    def __init__(self):
        super().__init__()
        super().setFixedSize(300, 200)
        self.seconds = [
            '1', '3', '5',
            '7', '9', '11',
            '13', '15', '30'
        ]
        self.positions = [(i, j) for i in range(3) for j in range(3)]

        self.msg_lbl = QLabel("好好想想你要做什么事！！")
        self.subDash = None

        self.init()
        self.setStyleSheet(style)

    def init(self):
        panel_lyt = QGridLayout()
        vbox_lyt = QVBoxLayout()
        alert_lyt = QHBoxLayout()

        for position, second in zip(self.positions, self.seconds):
            sec_btn = QPushButton(second, self)
            sec_btn.setObjectName('num-btn')
            sec_btn.clicked.connect(self.start)
            panel_lyt.addWidget(sec_btn, *position)

        self.msg_lbl.setAlignment(Qt.AlignCenter)
        self.msg_lbl.setStyleSheet('QLabel { background-color : #3c3f41; color: #FFFFFF}')
        alert_lyt.addWidget(self.msg_lbl)

        vbox_lyt.addLayout(panel_lyt) #上部数字
        vbox_lyt.addLayout(alert_lyt) #下部提示
        self.setLayout(vbox_lyt)
        center(self)

        self.setWindowTitle('TIME RUNS FAST!')
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.show()

    def start(self):
        source = self.sender()
        time = int(source.text()) * 60
        # self.hide()
        self.subDash = Dash(time, self)
        self.subDash.show()
        self.msg_lbl.setText('TIME IS OVER!!!! DONE? 笨蛋！ ' + str(time))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    sp = Sleep()
    sys.exit(app.exec_())

# TODOLIST
# 1. 有可能的话，将LCD字体居中
# 2. 记录日志到xls
# 3. 自定义时间button
