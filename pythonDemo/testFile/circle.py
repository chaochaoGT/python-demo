#!/usr/bin/evn python
# coding=utf-8

'Description:   '
__author__ = 'wang chao'



# utf-8


import turtle as t


#turtle.setup(width,height,startx,starty)设置窗体大小及位置，4个参数后两个可选。setup（）并不是必须的
t.setup(650,400,200,200)
t.penup()#海龟飞起
t.sety(-150)

t.pendown()#海龟落下
t.pensize(1)#画笔尺寸变为25
t.pencolor("black")#画笔颜色变为purple
t.circle(150,360)#设置40为半径，80°的弧度
t.penup()
t.sety(-125)
t.pendown()#海龟落下
t.circle(125,360)
t.penup()#海龟飞起
t.home()
i=0
while i<12:
    t.penup()
    t.home()
    t.pendown()#海龟落下

    t.setheading(30*(i+1))
    if i%2 == 0:
        t.fd(125)
    else:
        t.fd(150)
    i+=1
# t.fd(-250)#前进-250
#
# t.seth(-40)#方向设置为绝对-40°
# for i in range(4):  #循环4次
#     t.circle(40,80)#设置40为半径，80°的弧度
#     t.circle(-40,80)#设置反向40为半径，80°的弧度
#     t.circle(40,80/2)
#     t.fd(40)#行进40
#     t.circle(16,180)
#     t.fd(40*2/3)
t.done()#程序不会退出，需要手动退出
