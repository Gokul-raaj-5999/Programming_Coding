n,m= map(int, input().split())
arr= list(map(int, input().split()))

l=[]
for i in range(n):
    l.append([arr[i],i+1])
#print(l[0][1])
while(len(l)!=1):
        i=0
        if l[i][0]>m:
            l[i][0]-=m
            l.append(l[i])
        l.pop(i)
#print(l)
print(l[0][1])