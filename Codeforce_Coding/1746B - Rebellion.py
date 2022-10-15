def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = a.copy()
    b.sort()
    count = 0
    for i in range(0, n):
        if a[i]!= b[i]:
            count += 1

    return count //2


for t in range(0 ,int(input())):
    print(solve())