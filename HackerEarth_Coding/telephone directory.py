s = str(input())
s = "".join(sorted(s))
n = int(input())
count = 0
for item in range(0,n):
    x = str(input())
    x = "".join(sorted(x))
    flag = 1
    if(len(x)==len(s)):
        for i in range(0,len(x)):
            if(x[i]!=s[i]):
                flag = 0 
                break
        if(flag==1):
            count +=1        
print(count)
