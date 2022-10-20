def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    res = []
    for i in range(0, n):
        res.append([b[i], a[i], i])

    
    res.sort()
    # print(res)
    time = 0
    for i in range(0, n-1):
        a, h, pos = res[i]
        time += h
        res[i+1][1] += a

    time += res[-1][1]

    return time

for t in range(0, int(input())):
    print(solve())