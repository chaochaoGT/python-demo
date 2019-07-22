# utf-8

import json




def getNumb(x):
    nb=len(str(x))
    res='''%s%s'''%('0'*(12-nb),x)
    return res

try:
	
    bb = open("C:/Users/hc/Desktop/input.json",'r+',encoding='utf-8')


    a = open("C:/Users/hc/Desktop/output.json",'w+',encoding='utf-8')

    ids=[]

    numb=643
    while True:
	
        x=bb.readline()
		
        # print("##########################%s"%(f))
        if len(x)==0:
            break
        if x.strip()  in ids:
            continue
        else:
            ids.append(x.strip())
        # nn=getNumb(numb)

    if len(ids)>0:
        for id in ids:
            numb-=1
            a.write('''\n{\n"id":"%s",\n"score" : %s,\n"item_tags":"%s"\n}'''%(id,numb,"冷启动"))
            print("#############%s#############%s"%(id,getNumb(numb)))

except Exception as e:
    print(e)
finally:
    bb.close()
    a.close()

	



