n=int(input())
m=int(input())

for i in range(m):
	for g in range(n):
		if (g == 0) or (i==m-1) or (g==n-1) or (i ==0):
			if g==n-1 and i != 0 and i!= m-1:
				for b in range(n-2):
					print(" ",end="")
				print("A",end=" ")
				
			else:print("A",end="")
	print("")
