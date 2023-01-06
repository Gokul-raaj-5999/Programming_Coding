n, m = map(int, input().split())
a = []
for i in range(1, n+1):
    a.append(i)
i = 0
while i < len(a):
    if i%m == 0:
        a.append(a[-1]+1)
    i +=1
print(a[-1]-1)