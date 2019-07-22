
# utf-8


import turtle as t


#turtle.setup(width,height,startx,starty)设置窗体大小及位置，4个参数后两个可选。setup（）并不是必须的
t.setup(650,350,200,200)
t.penup()#海龟飞起
t.fd(-250)#前进-250
t.pendown()#海龟落下
t.pensize(25)#画笔尺寸变为25
t.pencolor("purple")#画笔颜色变为purple
t.seth(-40)#方向设置为绝对-40°
for i in range(4):  #循环4次
    t.circle(40,80)#设置40为半径，80°的弧度
    t.circle(-40,80)#设置反向40为半径，80°的弧度
    t.circle(40,80/2)
    t.fd(40)#行进40
    t.circle(16,180)
    t.fd(40*2/3)
t.done()#程序不会退出，需要手动