#!/usr/bin/python
# -*- coding: utf-8 -*-

from design.state import ConcreateStateB
from . import State

class ConcreteStateA(State):

    def handle(self, context):
        print('current state: %s', context.getState())
        context.setState(ConcreateStateB())
