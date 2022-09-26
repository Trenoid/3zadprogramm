const=9
for i in range(1,const+1):
	for g in range(1,const+1):
		if i*g>9:
			print(i,"*",g,"=",i*g,end="  ")
		else: print(i,"*",g,"=",i*g,end="   ")
	print("")
	