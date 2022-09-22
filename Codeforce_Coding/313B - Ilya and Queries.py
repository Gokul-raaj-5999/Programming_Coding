l=input()
t=[0]
n=len(l)
s=0
for i in range(1,n):
	if l[i]==l[i-1]:
		s+=1
	t.append(s)
for i in range(int(input())):
	l,r=map(int,input().split())
	print(t[r-1]-t[l-1])