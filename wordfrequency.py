data=input('ENTER THE STRING VALUE: ')
dt={}
for x in data:
	if x in dt.keys():
		dt[x]+=1
	else:
		dt[x]=1
print(dt)