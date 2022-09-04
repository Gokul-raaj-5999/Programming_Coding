input1=input()

a=list()
for i in input1:
    a.append(i)
a.sort()
count=1
out=''
for i in range(1,len(a),1):
    if(a[i]!=a[i-1]):
        out+=a[i-1]+str(count)
        count=1
    else:
        count+=1
out+=a[i]+str(count)
print(out)