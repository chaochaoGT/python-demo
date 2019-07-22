#!/usr/bin/evn python
# coding=utf-8
import threading
from pymongo import MongoClient


conn = MongoClient('172.16.11.251', 27017)

db = conn['laowang']  #连接mydb数据库，没有则自动创建
my_set = db['lw-media-source-6-19']  #使用test_set集合，没有则自动创建




try:
    bb= open("C:/Users/hc/Desktop/laowang.lw-media-source-6-19-del -(1).json",'w+',encoding='utf-8')
    for i in my_set.find({}):
        # print(i)
        obj=i
        id= i['id']



        # print(author)
        inster=''''%s'\n'''%(id)
        bb.write(inster)
        print(inster)
except Exception as e:
    print(e)

# threading.Timer(5, printHello).start()