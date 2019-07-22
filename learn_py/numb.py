def getNumb(x):
	nb=len(str(x))
	res='''%s%s'''%('0'*(12-nb),x)
	return res




print(getNumb(12))
