#!/usr/bin/python
# -*- coding: utf-8 -*-

## 状态模式 + 模板模式
from . import  Context

class State(object):
    def handle(self, context):
        pass
























        # def __init__(self):
    #     self.nextState = None
    #     self.context = None
    #
    # # 关联状态， 类似于职责链模式， 装饰模式
    # def setNextState(self, state):
    #     self.nextState = state



    # def stateHandle(self, context):
    #     self.handle(context)


# 状态模式 + 职责连模式 ＋ 命令模式 + 建造者模式

#　职责链模式
#
# class State():
#     def __init__(self):
#         self.nextState = None
#
#     # 关联状态， 类似于职责链模式， 装饰模式
#     def setNextState(self, state):
#         self.nextState = state
#
#     def handle(self):
#         pass
#
#     def stateHandle(self):
#
#         self.handle()
#
#         if self.nextState: ## 如果本职责不能处理，交给下一个
#             self.nextState.stateHandle(self.nextState)

