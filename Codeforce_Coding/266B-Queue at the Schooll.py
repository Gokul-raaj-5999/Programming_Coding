n , t = map(int, input().split())
s = str(input())
ar = []
for i in s:
    ar.append(i)
for _ in range(t):
    i = 0
    while(i < len(s)-1):
        if(ar[i]=='B' and ar[i+1]=='G'):
            ar[i] = "G"
            ar[i+1] = "B"
            i+=2
        else:
            i+=1
s = ''
for i in ar:
    s+=i
print(s)
