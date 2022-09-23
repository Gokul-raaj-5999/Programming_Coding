n = int(input())
v = list(map(int, input().split()))
m = int(input())
a = [v[0]]
for i in range(1, n):
    a.append(a[-1]+ v[i])
# print(a)
v.sort()
b = [v[0]]
for i in range(1, n):
    b.append(b[-1] + v[i])
# print(b)

for _ in range(0, m):
    type, l, r = list(map(int, input().split()))
    r -= 1
    l -= 1
    if type == 1:
        if l == 0:
            print(a[r])
        else:
            print( a[r] - a[l-1])
    else:
        if l == 0:
            print(b[r])
        else:
            print( b[r] - b[l-1])