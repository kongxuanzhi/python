#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

from Buttons import ImageButton
from Utils import *
from PyQt5.QtCore import Qt, QBasicTimer, QSize
from PyQt5.QtGui import QPainter, QIcon, QCursor
from PyQt5.QtWidgets import (QTextEdit,QLineEdit,
                             QComboBox)


style = '''
QPushButton#count-down-btn {
    background-color: #3c3f41;
    color: #ffffff;
    border-style: outset;
    border-width: 2px;
    border-radius: 10px;
    border-color: beige;
    font: bold 14px;
    min-width: 5em;
    padding: 6px;  
}

QPushButton#count-down-btn::hover {
    background-color: red;   
}

QPushButton#toggle-btn {
    color: grey;
    border-image: url(./clock/round_right_fill.png) 3 10 3 10;
    border-top: 3px transparent;
    border-bottom: 3px transparent;
    border-right: 10px transparent;
    border-left: 10px transparent;  
}

QPushButton#toggle-btn::hover {
    
}
'''


class CountDown(QWidget):
    def __init__(self, time, parent_board):
        super().__init__()
        self.setFixedSize(100, 60)
        self.lcd = QLCDNumber(self)
        self.status_btn = ImageButton('./clock/stop.png', './clock/play_fill.png', '', self)
        self.status_btn.setSize(QSize(25, 25))

        self.timer = QBasicTimer()
        self.time = time
        self.isPause = False
        self.parentBoard = parent_board
        self.init()

    def init(self):
        main_layout = QHBoxLayout(self)
        main_layout.addWidget(self.status_btn)
        main_layout.addWidget(self.lcd, Qt.AlignCenter)

        self.status_btn.connect(self.changeStatus)
        self.timer.start(1000, self)

        self.move(3000, 1000)
        self.setStyleSheet("QWidget { background-color: #3c3f41 }")
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.show()

    def changeStatus(self):
        if not self.status_btn.isPress:
            self.timer.start(1000, self)

    def timerEvent(self, e):
        # 如果按下了，或者时间到了
        self.lcd.display(self.time)
        timeOver = self.calcTime()
        if self.status_btn.isPress or timeOver:
            self.timer.stop()
            self.parentBoard.log(self.time)
            if timeOver:
                self.hide()
                self.parentBoard.show()
            return

    # 默认倒计时
    def calcTime(self):
        self.time = self.time - 1
        return self.time == 0


class Timing(CountDown):
    def __init__(self, time, parent_board):
        super().__init__(time, parent_board)

    # 正计时
    def calcTime(self):
        self.time = self.time + 1
        return self.status_btn.isPress


class Sleep(QWidget):
    def __init__(self):
        super().__init__()
        super().setFixedSize(340, 300)
        self.seconds = [
            '1', '2', '3',
            '5', '8', '13',
            '15', '20', '30',
            '21', '34', '55'
        ]
        self.positions = [(i, j) for i in range(4) for j in range(3)]
        self.startTime = self.endTime = None
        self.time = 0
        self.items = []

        self.isPress = False

        self.left = QWidget(self)
        self.right = QWidget(self)
        self.msg_lbl = QLabel("好好想想你要做什么事！！")
        self.todolist_cbb = QComboBox()
        self.todolist_tb = QLineEdit()

        self.tdl_file = None

        self.subWin = None

        self.init()
        self.setStyleSheet(style)

    def init(self):
        # toggle = QPushButton('', self)
        # toggle.setObjectName('toggle-btn')
        # toggle.setFixedSize(30, 30)
        # toggle.move(300, 10)
        # self.right.show()
        # super().setFixedSize(800, 300)
        # self.right.hide()
        # super().setFixedSize(340, 300)
        # center(self)

        main_panel = QHBoxLayout()
        right_panel = QVBoxLayout()
        left_panel = QVBoxLayout()

        # left top
        num_top_panel = QGridLayout()
        for position, second in zip(self.positions, self.seconds):
            sec_btn = QPushButton(second, self)
            sec_btn.setCursor(QCursor(Qt.PointingHandCursor))
            sec_btn.setObjectName('count-down-btn')
            sec_btn.clicked.connect(self.start)
            num_top_panel.addWidget(sec_btn, *position)
        sec_btn = QPushButton('Start', self)
        sec_btn.setCursor(QCursor(Qt.PointingHandCursor))
        sec_btn.setObjectName('count-down-btn')
        sec_btn.setIcon(QIcon('stop.png'))
        sec_btn.clicked.connect(self.start)
        num_top_panel.addWidget(sec_btn, 4, 0, 1, 3)

        # left bottom
        self.msg_lbl.setAlignment(Qt.AlignCenter)
        self.msg_lbl.setStyleSheet('QLabel { background-color : #3c3f41; color: #FFFFFF}')
        self.loadTodDoList()

        msg_bottom_panel = QVBoxLayout()
        msg_bottom_panel.addWidget(self.msg_lbl)
        msg_bottom_panel.addWidget(self.todolist_tb)
        msg_bottom_panel.addWidget(self.todolist_cbb)

        # left
        left_panel.addLayout(num_top_panel)  # 上部数字
        left_panel.addLayout(msg_bottom_panel)  # 下部提示

        # right top ---------------------
        textEdit = QTextEdit()
        add_tbd_top_panel = QVBoxLayout()
        add_tbd_top_panel.addWidget(textEdit)

        # right bottom
        add_tbd_bottom_panel = QVBoxLayout()

        # right
        right_panel.addLayout(add_tbd_top_panel)
        right_panel.addLayout(add_tbd_bottom_panel)


        # main
        self.right.setLayout(right_panel)
        self.left.setLayout(left_panel)

        main_panel.addWidget(self.left)
        main_panel.addWidget(self.right)

        self.setLayout(main_panel)
        # right_widget.hide()
        # main_panel.removeItem(right_panel)
        # right_panel.setParent(None)
        # main_panel.invalidate()
        # # self.setLayout(main_panel)
        self.right.hide()
        center(self)
        self.setWindowTitle('TIME RUNS FAST!')
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.show()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        qp.setPen(Qt.blue)
        qp.drawPoint(300, 10)
        qp.end()

    def start(self):
        source = self.sender()
        try:
            self.time = int(source.text()) * 60
            self.subWin = CountDown(self.time, self)
        except ValueError:
            self.subWin = Timing(0, self)

        self.hide()
        self.saveToDoList(self.todolist_tb.text())
        self.startTime = getCurrentTime()
        self.subWin.show()
        self.msg_lbl.setText('TIME IS OVER!!!! DONE? 笨蛋！ ' + str(self.time))


    #load for first time
    def loadTodDoList(self):
        self.tdl_file = open('./clock/todolist.txt', 'r')
        list = self.tdl_file.readlines()
        print(list)
        for line in list:
            self.todolist_cbb.addItem(line.strip('\n'))
        self.tdl_file.close()

    def saveToDoList(self, text):
        # save text to file and add text to list
        # not in list then add & save, then load
        if text:
            self.todolist_cbb.addItem(text)
            self.tdl_file = open('./clock/todolist.txt', 'a')
            self.tdl_file.write(text + "\n")
            self.tdl_file.close()

    def log(self, time):
        currentDoing = self.todolist_cbb.currentText()
        text = self.todolist_tb.text()
        if text:
            currentDoing = text

        self.endTime = getCurrentTime()
        strTime = str(time) + "\t total:" + str(self.time) if time == 0 else str(time)
        fmt = currentDoing + ':\t' + self.startTime + "--->" + self.endTime + "\t" + strTime
        log_file = open('./clock/log.txt', 'a')
        log_file.write(fmt + "\n")
        log_file.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    sp = Sleep()
    sys.exit(app.exec_())

# TODOLIST
# 2. 记录日志到xls
# 3. 自定义时间button  done
# 4. 选中默认事件，计时
# 5. 计时
# 6. 添加tag 如，某个项目， build，等
