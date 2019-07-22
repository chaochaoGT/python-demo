#!/usr/bin/evn python
# coding=utf-8

'Description:   '
__author__ = 'wang chao'


class Car(object):
    def move(self):
        print("moving")
    def run(self):
        print("running")
    def stop(self):
        print("stopping")


class Xiandai(Car):
    pass


class Baoma(Car):
    pass


class Aodi(Car):
    pass


class CarStore(object):
    def __init__(self):
        self.factory=SelectCar()

    def order(self,type):
        self.type=type
        return self.factory.getCar(self.type)


class SelectCar(object):
    def getCar(slfe,type):
        if type=='1':
            return Xiandai()
        elif type=="2":
            return Baoma()
        elif type=="3":
            return Aodi()




car_store = CarStore()

car=car_store.order("1")

car.run()