#!/usr/bin/python
# -*- coding: utf-8 -*-

class Context(object):
    def __init__(self, state): #初始状态
        self.state = state

    def changeState(self):
        self.state.handle(self)

    def setState(self, state):
        self.state = state

    def getState(self):
        return self.state

