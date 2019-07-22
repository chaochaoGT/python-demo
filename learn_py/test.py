# utf-8

import json




def getNumb(x):
	nb=len(str(x))
	res='''%s%s'''%('0'*(12-nb),x)
	return res


try:
	
	bb = open("C:/Users/hc/Desktop/daguan_ids.txt",'r+')


	a = open("C:/Users/hc/Desktop/output.json",'w+')


	numb=0
	# while True:
	
		# x=bb.readline()
		# print(x)
	for i, x in enumerate(bb):
		# print(x)
		f=x.find("id")
		# print(f)
		if x.find("id")<6:
			a.write(x)
	
		
except Exception as e:
	print(e)
finally:
	bb.close()
	a.close()

	



# for i, x in enumerate(b):
# 	x=x.strip()
# 	a.write("我想玩 %s  %s 次\n "%(x,i))	

# a.close()
