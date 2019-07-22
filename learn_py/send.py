class Send:
	type = 0

	def __send(self):
		print("正在发送短信")



	def test(self):
		self.__send()

		print("test is hear")


	@classmethod
	def chageType(cls):
		cls.type =1


	@staticmethod
	def static_menu():
		print("static  ")


		


send =Send()
send.static_menu()
print(Send.type)
Send.chageType()
print(Send.type)
send.test()