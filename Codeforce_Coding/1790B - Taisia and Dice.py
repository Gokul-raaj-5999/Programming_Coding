def func(m, n ,r):
    op = []
    for i in range(0, n):
        op.append(r // (n-i))
        r -= op[-1]
    return op

def solve():
    n, s, r = list(map(int, input().split()))

    miss = s - r
    mele = miss
    rele = n-1

    arr = func(mele, rele ,r)
    arr.append(miss)

    print(' '.join(str(x) for x in arr))

for t in range(0, int(input())):
    solve()