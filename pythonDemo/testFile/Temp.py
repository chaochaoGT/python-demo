#!/usr/bin/evn python
# coding=utf-8






def prt(name,qq,tel,addr):
    # text="=========================\n姓名：%s  年龄；%d  tel:%s" %(name,  age, tel)

    aa = '''
    ==================================
    姓名: %s    
    QQ:%s
    手机号:%s
    公司地址:%s
    ==================================
    ''' %(name,qq,tel,addr)

    print(aa)


if __name__ == '__main__':
    name=input("name...")
    qq=input("qq...")
    tel=input("tel...")
    addr=input("addr...")

    prt(name, qq, tel, addr)
