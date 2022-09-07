n = int(input())
a = list(map(int,input().split()))
pos = 1
a.sort()

for i in range(0, n):
    if a[i] >= pos:
        pos += 1

print(pos-1)
