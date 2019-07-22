#!/usr/bin/evn python
# coding=utf-8
import threading
from pymongo import MongoClient

conn = MongoClient('172.16.11.251', 27017)

db = conn['laowang']  #连接mydb数据库，没有则自动创建
my_set = db['lw-media-source']  #使用test_set集合，没有则自动创建




try:
    bb= open("C:/Users/hc/Desktop/icon.txt",'w+',encoding='utf-8')
    for i in my_set.find({"duration":{"$lte":"02:30","$gte":"00:30"},"is_delete":0}).skip(
            50000).limit(200):
        # print(i)
        obj=i
        author= i['author']

        avatar = author["avatar"]


        # print(author)
        if not avatar.startswith("http"):
            inster='''INSERT INTO `laowang_media`.`lw_v2_icon_pool` ( `icon_url`) VALUES ('%s');\n'''%(avatar)
            bb.write(inster)
            print(inster)
except Exception as e:
    print(e)

# threading.Timer(5, printHello).start()