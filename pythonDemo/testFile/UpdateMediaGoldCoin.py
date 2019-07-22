#!/usr/bin/evn python
# coding=utf-8

'Description:   '
__author__ = 'wang chao'

#!/usr/bin/evn python
# coding=utf-8
import threading
from pymongo import MongoClient

conn = MongoClient('172.16.11.247', 27017)

db = conn['laowang']  #连接mydb数据库，没有则自动创建
my_set = db['lw-media-source']  #使用test_set集合，没有则自动创建




pageNumb =0;
pageSize=1000;

for i in my_set.find().skip(2).limit(6):
    print(i)



threading.Timer(5, printHello).start()