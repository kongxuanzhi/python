#!/usr/bin/python
# -*- coding: utf-8 -*-

from . import ConcreateStateA
from . import State

class ConcreteStateB(State):

    def handle(self, context):
        print('current state: %s', context.getState())
        context.setState(ConcreateStateA())
