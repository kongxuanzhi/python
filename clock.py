#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import (QWidget, QGridLayout, QVBoxLayout, QFrame,QLabel,
                             QHBoxLayout, QPushButton, QApplication, QLCDNumber
                             , QDesktopWidget)
# from PyQt5.QtGui import QPainter, QFont, QColor, QPen
from PyQt5.QtCore import Qt, QBasicTimer
from Utils import center

class Dash(QWidget):
    def __init__(self, time, parent_board):
        super().__init__()
        self.setFixedHeight(60)
        self.setFixedWidth(100)
        self.lcd = QLCDNumber(self)
        self.timer = QBasicTimer()
        self.time = time
        self.parentBoard = parent_board
        self.init()

    def init(self):
        main_layout = QHBoxLayout(self)
        main_layout.addWidget(self.lcd, Qt.AlignCenter)
        self.timer.start(1000, self)

        self.move(2000, 2000)
        self.setStyleSheet("QWidget { background-color: #3c3f41 }")
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.show()

    def timerEvent(self, e):
        if self.time == 0:
            self.timer.stop()
            self.hide()
            self.parentBoard.show()
            return

        self.time = self.time - 1
        self.lcd.display(self.time)

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
        self.init()
        self.subDS = None

    def init(self):
        panel_lyt = QGridLayout()
        vbox_lyt = QVBoxLayout()
        alert_lyt = QHBoxLayout()

        for position, second in zip(self.positions, self.seconds):
            sec_btn = QPushButton(second, self)
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
        self.hide()
        self.subDS = Dash(time, self)
        self.subDS.show()
        self.msg_lbl.setText('TIME IS OVER!!!! DONE? 笨蛋！ ' + str(time))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    sp = Sleep()
    sys.exit(app.exec_())

# TODOLIST
# 1. 有可能的话，将LCD字体居中
# 2. 记录日志到xls
# 3. 自定义时间button
