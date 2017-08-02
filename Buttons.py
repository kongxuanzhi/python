#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QPainter, QColor, QImage, QBrush, QCursor, QFont
from PyQt5.QtCore import Qt, QRect, QPoint, QSize


class ImageButton(QPushButton):

    def __init__(self, icon_down, icon_up, text, parent=None):
        super().__init__(text, parent)
        self.isPress = False
        self.f = None
        self.size = self.frameSize()
        self.backColor = QColor('#3c3f41')

        self.icon_down = QImage(icon_down)
        self.icon_up = QImage(icon_up)
        self.setCursor(QCursor(Qt.PointingHandCursor))
        self.clicked.connect(self.changeState)

    def setSize(self, size):
        self.size = size
        self.setFixedSize(size)

    def setBackColor(self, color='#3c3f41'):
        self.backColor = QColor(color)

    def paintEvent(self, QPaintEvent):
        qRect = QRect(QPoint(0,0), self.size)

        painter = QPainter(self)
        painter.fillRect(qRect, QBrush(self.backColor))

        if self.isPress:
            #painter.drawText(0, 0, '121')
            painter.drawImage(qRect, self.icon_up)
        else:
            # QPainter.drawText(int, int, str)
            painter.drawImage(qRect, self.icon_down)

    def connect(self, f):
        self.f = f

    def changeState(self):
        self.isPress = not self.isPress
        if self.f:
            self.f()

class TextButton(QPushButton):
    def __init__(self, text, backColor, foreColor, parent=None):
        super().__init__(text, parent)
        self.backColor = backColor
        self.foreColor = foreColor

    def mouseMoveEvent(self, e):
        self.foreColor = QColor('#fff555')

    def paintEvent(self, QPaintEvent):
        qRect = QRect(QPoint(0, 0), QSize(self.width(), self.height()))
        painter = QPainter(self)
        painter.fillRect(qRect, QBrush(QColor(self.backColor)))
        painter.setPen(QColor(self.foreColor))
        painter.drawText(qRect, Qt.AlignCenter, self.text())

