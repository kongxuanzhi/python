#!/usr/bin/python
# -*- coding: utf-8 -*-

# 职责链模式 > 包含状态模式 + 建造者模式
# 多个状态

import Context
import ConcreateStateA

if __name__ == '__main__':
    context = Context(ConcreateStateA())
    context.changeState()
    context.changeState()
    context.changeState()

