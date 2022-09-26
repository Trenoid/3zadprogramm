n = int(input())
m=0
s = 0
k=n
for i in range(1,n+1):
	s+=k
	k*=n
print(s)
