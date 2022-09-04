n=int(input("size: "))
numbers=[]
for i in range(n):
    numbers.append(int(input()))


num={}
count=0
for i in numbers:
    num[i]=num.get(i,0)+1
for i in num.values():
    if(i>1):
        count+=1
print(count)
    