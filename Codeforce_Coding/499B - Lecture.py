n, m = map(int, input().split())
dic = {}
for i in range(0, m):
    a, b = map(str, input().split())
    if len(a) < len(b):
        dic[a] = a
        dic[b] = a
    elif len(a) > len(b):
        dic[a] = b
        dic[b] = b
    else:
        dic[a] = a
        dic[b] = b
arr = list(map(str, input().split()))
op = []
for i in arr:
    op.append(dic[i])

print(' '.join(x for x in op))
