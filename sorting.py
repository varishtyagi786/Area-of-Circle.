from random import shuffle
ls=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
shuffle(ls)
for x in range(len(ls)):
	i=x
	for y in range(i+1,len(ls)):
		if ls[i]>ls[y]:
			i=y
	ls[x],ls[i]=ls[i],ls[x]
print(ls)