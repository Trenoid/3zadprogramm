n = int(input())
x = float(input())
s=0
m=1
b = 1

for k in range(1,n+1):
	m=m*k 
	b*=x 
	s+=m*b
print(s)