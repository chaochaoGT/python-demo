#!/usr/bin/evn python
# coding=utf-8

'Description:   '
__author__ = 'wang chao'


def crm(y):

    x = 1
    z=5
    while y < 10:
        if x < 5:
            print('*'*x)
            x += 1
        else:
            # print(p)
            print('*'*z)
            z -= 1
        y += 1


if __name__ == '__main__':
    crm(0)
