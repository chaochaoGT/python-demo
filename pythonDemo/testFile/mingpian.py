#!/usr/bin/evn python
# coding=utf-8

'Description:   '
__author__ = 'wang chao'

dec = []


def add_card_info():
    a = {}
    name = input("====输入名称\n")
    tel = input("====输入tel\n")
    a['name'] = name
    a['tel'] = tel
    # global dec
    dec.append(a)
    return a


def update_card_by_name():
    a = {}

    name = input("====输入修改前名称\n")
    name2 = input("====输入修改后名称\n")
    tel = input("====输入tel\n")

    a['name'] = name2
    a['tel'] = tel
    for i, x in enumerate(dec):
        if x['name'] == name:
            dec[i] = a
        else:
            continue


def del_card_by_name():
    '通过姓名删除card'
    name = input("====输入要删除的名称\n")
    for i, x in enumerate(dec):
        if x['name'] == name:
            del dec[i]
        else:
            continue


def find_card_by_name():
    name = input("====输入要查找的名称\n")
    find_flag=False
    for i, x in enumerate(dec):
        if x['name'] == name:
            print("找到了"+str(x))
            find_flag=True
        else:
            continue
    if not find_flag:
        print("未找到该用户！！！")



def addDic():
    '名片系统'
    while True:
        type = int(input('''
        名片系统：
            1：add
            2：update
            3：delete
            4：find
            5：exit—sys\n\n\n
        '''))
        if 1 == type:
            add_card_info()
        elif 2 == type:
            # for x in dec:
            #    x.values()
            update_card_by_name()
        elif 3 == type:
            del_card_by_name()

        elif 4 == type:
            find_card_by_name()
        elif 5 == type:
            print("推出系统")
            break
        getDec()


def getDec():
    print("dec %s" % dec)



addDic()