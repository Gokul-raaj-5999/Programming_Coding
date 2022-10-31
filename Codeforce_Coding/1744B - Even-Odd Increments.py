def solve():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    ec = 0
    oc = 0
    sum = 0

    for i in a:
        sum += i
        if i%2 == 0:
            ec += 1
        else:
            oc += 1
    
    for i in range(q):
        t, x = map(int, input().split())
        if t == 0:
            sum += ec*x
            if x%2 != 0:
                ec =0
                oc = n
        else:
            sum += oc*x
            if x%2 != 0:
                ec = n
                oc = 0
        print(sum)


for t in range(0, int(input())):
    solve()