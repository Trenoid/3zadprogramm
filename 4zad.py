n = int(input())
s=0
m=1

for i in range(1,n+1):
	s+=m*2
	m=m*2
print(s)
