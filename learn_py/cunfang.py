class Home():
	"""docstring for Home"""
	area_totle=0
	def __init__(self,info,area,addr):
		self.info=info
		Home.area_totle=area
		self.area=area
		self.addr=addr
		self.thing_list=[]


	def add_thing(self,item):
		if item.area<=self.area:
			iteminfo={}
			iteminfo['name']=item.name
			iteminfo['area']=item.area
			self.thing_list.append(item.__str__())
			self.area-=item.area
		else:
			print("当前物品面积%d大于房屋剩余面积%d"%(item.area,self.area))


	def __str__(self):
		return '''当前房屋%s 总面积%d 剩余面积%d \n 房屋物品%s'''%(self.info,Home.area_totle,self.area,str(self.thing_list))


class Bad(object):
	"""docstring for bad"""
	def __init__(self, name,area):
		self.name = name
		self.area=area
	def __str__(self):
		return "物品名称%s  占用面积%d"%(self.name,self.area)

fangzi=Home("三室两厅两卫",130,"西安市 西咸区 丈八路")

bad1=Bad("大床",10)
bad2=Bad("中床",8)
bad3=Bad("小床",5)

fangzi.add_thing(bad1)
print(fangzi)
fangzi.add_thing(bad2)
print(fangzi)

fangzi.add_thing(bad3)
print(fangzi)

		