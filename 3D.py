#-*- coding:utf-8 -*-
__author__ = '孔轩志'


from turtle import *
from numpy import *
from math import  *
from copy import *

len = 30


def  hua(start1):
    start = deepcopy(start1)
    for i in range(8):
        start[i][2] = 0
    for i in range(8):
        goto(start[i][0],start[i][1])
    for i in range(3):

        penup()
        goto(start[i][0],start[i][1])
        pendown()
        goto(start[7-i][0],start[7-i][1])

    penup()
    goto(start[0][0],start[0][1])
    pendown()
    goto(start[3][0],start[3][1])

    penup()
    goto(start[4][0],start[4][1])
    pendown()
    goto(start[7][0],start[7][1])

def rotate(start,degree=20,dir="x"):
    if(dir =="x"):
        rotatex = array([[1,0,0,0],
                     [0,cos(degree),sin(degree),0],
                     [0,-sin(degree),cos(degree),0],
                     [0,0,0,1]])
        return dot(start,rotatex)
    if dir == "y":
        rotatey = array([[cos(degree),0,-sin(degree),0],
                 [0,1,0,0],
                 [sin(degree),0,cos(degree),0],
                 [0,0,0,1]])
        return dot(start,rotatey)


start = array([[0,0,0,1],[len,0,0,1],[len,len,0,1],[0,len,0,1],
               [0,len,len,1],[len,len,len,1],[len,0,len,1],[0,0,len,1]])

start = rotate(start,45,"x")
start = rotate(start,45,"y")
hua(start)

for i in range(1,30):
    reset()
    start = rotate(start,0.3*i,"x")
    hua(start)

input()




