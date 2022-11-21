def solve():
    n = int(input())
    a= list(map(int, input().split()))
    b = a.copy()
    b.sort()
    m = b[-1]
    n = b[-2]

    op = []
    for i in a:
        if m - i == 0:
            x = n - i
            op.append(-1*x)
        else:
            x = m - i
            op.append(-1*x)
    print(' '.join(str(x) for x in op))



for t in range(0, int(input())):
    solve()