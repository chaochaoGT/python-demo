#!/usr/bin/evn python
# coding=utf-8

'Description:   猜拳'
__author__ = 'wang chao'

import random

s = 0  # 石头
j = 1  # 剪刀
b = 2  # 布


def inputNumb(x, randomNumb):
    if ((x == s) and (randomNumb == j)) or ((x == j) and (randomNumb == b)) or ((x == b) and (randomNumb == s)):
        print("胜")
    elif ((x == s and randomNumb == s) or (x == j and randomNumb == j) or (x == b and randomNumb == b)):
        print("平")
    elif ((x == s and randomNumb == b) or (x == j and randomNumb == s) or (x == b and randomNumb == j)):
        print("你败了")
    else:
        print("你耍赖")


if __name__ == '__main__':
    while True:
        try:
            x = input('''欢迎猜拳游戏：
                  0 ====石头    1 ====剪刀  2 ====布 \n '''
                      )
            randomNumb = random.randint(0, 2)
            inputNumb(int(x), randomNumb)
            print("本局结束**********************************\n")
        except ValueError:
            print("输入无效！请正常操作 ")
