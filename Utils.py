#!/bin/python
# -*- coding:utf-8 -*-

from PyQt5.QtWidgets import (QWidget, QGridLayout, QVBoxLayout, QFrame,QLabel,
                             QHBoxLayout, QPushButton, QApplication, QLCDNumber
                             , QDesktopWidget)

def center(qw): # for qwidget
    qr = qw.frameGeometry()
    cp = QDesktopWidget().availableGeometry().center()
    qr.moveCenter(cp)
    qw.move(qr.topLeft())

