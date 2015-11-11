# -*- coding:utf-8 -*-
__author__ = '孔轩志'

from turtle import *
from numpy import *
from math import *

begin_fill()
# for i in range(5):
#     if i==0:
#         rt(36)
#     else:
#         rt(72)
#     fd(100)
#     lt(144)
#     fd(100)
#
# end_fill()
#画个矩形并作平移旋转，放大错切等变换

#根据四个点画出一个图形


def initCord():
    penup()
    sety(-150)
    pendown()
    sety(250)
    #rt(90)
    fd(5)
    lt(120)
    fd(10)
    lt(120)
    fd(10)
    lt(120)
    fd(5)
    home()
    penup()
    setx(-150)
    pendown()
    setx(250)
    rt(90)
    fd(5)
    lt(120)
    fd(10)
    lt(120)
    fd(10)
    lt(120)
    fd(5)
    home()

def rect(point=[]):
    #reset()
    penup()
    setpos(point[0][0],point[0][1])
    #clear()
    pendown()
    for i in range(len(point)-1):
        goto(point[i+1][0],point[i+1][1])
    goto(point[0][0],point[0][1])


def goline(point=[],dx=0,dy=0):
    goMat = array([[1,0,0],[0,1,0],[dx,dy,1]])
    for i in range(len(point)):
        point[i] = dot(array(point[i]), goMat)
    return point

def rotate(point=[],angle=0):
    roMat = array([[cos(angle),sin(angle),0],[-sin(angle),cos(angle),0],[0,0,1]])
    for i in range(len(point)):
        point[i] = dot(array(point[i]), roMat)
    return point

def opsist(point=[],axis="x"):
    opMat = array([[1,0,0],[0,-1,0],[0,0,1]])
    for i in range(len(point)):
        point[i] = dot(array(point[i]),opMat)

    return point

def big(point=[],dx=0,dy=0):
    bMat=[[dx,0,0],[0,dy,0],[0,0,1]]
    for i in range(len(point)):
        point[i] = dot(array(point[i]),bMat)
    return point


initCord()

penup()
goto(150,-100)
pendown()
goto(-100,150)
penup()
home()
pendown()

start = [[0, 150,1],[200, 150,1],[200, 40,1]]#,[150,-100,1],[-100,150,1]]#,[-100,-100,1]  #[50, 250,1],[250, 250,1],[250, 140,1]
rect(start)
print(start)

point = big(start,2,2)   #放大
rect(point)
print(point)

point = big(start,0.1,0.1)   #缩小
rect(point)
print(point)



point = goline(start,-50,0)    #平移到原点
print(point)
# rect(point)

# point = rotate(point,pi/4) #旋转与x轴重合
# print(point)
# # rect(point)

point = opsist(point)  #做对称
print(point)
# rect(point)

# point = rotate(point,-pi/4)  #旋转回去
# print(point)
# # rect(point)

point = goline(start,50,0)   #平移回去
print(point)
#rect(point)

input()
pause