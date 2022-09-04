n = int(input())
p = list(map(int, input().split()))
b = list(map(int, input().split()))
i = 0
j = 0
p.sort()
b.sort()
count = 0
while (j<n):
    if(p[i]<=b[j]):
        count+=1
        i+=1
        j+=1
    else:
        j+=1
print(count)
