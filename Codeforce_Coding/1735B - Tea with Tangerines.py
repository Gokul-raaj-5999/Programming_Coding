import math


def solve():
    n = int(input())
    a = list(map(int, input().split()))
    n = a[0]
    m = 2*n -1
    count = []
    for i in a:
        if i < m:
            continue
        else:
            q = math.ceil(i/m)
            # print(i, q)
            count.append(q-1)
    # print(count)
    return sum(count)

for t in range(0, int(input())):
    print(solve())
    # print()