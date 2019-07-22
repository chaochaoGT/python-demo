# utf-8

import json




def getNumb(x):
	nb=len(str(x))
	res='''%s%s'''%('0'*(12-nb),x)
	return res


try:
	
	bb = open("C:/Users/hc/Desktop/lw-media-field-up-backup-2019-05-09.json",'r+',encoding='utf-8')


	a = open("C:/Users/hc/Desktop/output.json",'w+')


	numb=0
	while True:
	
		x=bb.readline()
		f=x.find("url")
		# print("##########################%s"%(f))
		if len(x)==0:
			break
		if (x.find("url")>11):
			print("##########################%s"%(f))
			a.write(x.replace("repairData", "xxxx"))
			# print(x)
				

			numb+=1

			print("i=%s %s f=%s"%(numb,x.strip(),f))

		else:
			# print(x)
			a.write(x)
	
		
except Exception as e:
	print(e)
finally:
	bb.close()
	a.close()

	



