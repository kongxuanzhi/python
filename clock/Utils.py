#!/bin/python
# -*- coding:utf-8 -*-

from PyQt5.QtWidgets import (QWidget, QGridLayout, QVBoxLayout, QFrame,QLabel,
                             QHBoxLayout, QPushButton, QApplication, QLCDNumber
                             , QDesktopWidget)
import time

def center(qw):
    qr = qw.frameGeometry()
    cp = QDesktopWidget().availableGeometry().center()
    qr.moveCenter(cp)
    qw.move(qr.topLeft())

def getCurrentTime():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())