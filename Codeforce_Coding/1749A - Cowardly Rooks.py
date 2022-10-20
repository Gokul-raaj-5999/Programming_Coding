def solve():
    n, m = map(int, input().split())
    a = []
    r, c = [], []
    rr, cc = [], []
    for i in range(1, n+1):
        r.append(i)
        c.append(i)

    for i in range(0, m):
        x,y = list(map(int, input().split()))
        a.append([x,y])
        rr.append(x)
        cc.append(y)
    
    ans1 = set(r) - set(rr)
    ans2 = set(c) - set(cc)

    if ans1 and ans2:
        return 'YES'
    else:
        return 'NO'
    
    



for t in range(0, int(input())):
    print(solve())