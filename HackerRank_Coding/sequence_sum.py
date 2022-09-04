i=int(input())
j=int(input())
k=int(input())

tot=0
for s in range(i,j+1,1):
    tot+=s
for s in range(j-1,k-1,-1):
    tot+=s
return(tot)