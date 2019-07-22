class Game:

	# 类属性
	num=0

	# 实例方法
	def __init__(self,new_name):
		# 实例属性
		self.name=new_name


	# @Classmethod
	def add_num(self,mew_num):
		Game.num+=mew_num
	def __str__(self):
		return "info: name=%s num=%d"%(self.name,Game.num)

game=Game("chao")		
game.add_num(100)
print(str(game))

game=Game("chao1")		
game.add_num(1)
print(str(game))
game=Game("chao1")		
game.add_num(1)
print(str(game))
game=Game("chao1")		
game.add_num(1)
print(str(game))
game=Game("chao1")		
game.add_num(1)
print(str(game))