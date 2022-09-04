n, h = map(int, input().split())
per = list(map(int, input().split()))
width = 0
for i in per:
    if i <= h:
        width+=1
    else:
        width+=2
print(width)