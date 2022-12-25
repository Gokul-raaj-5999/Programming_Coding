def solve():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()

    for i in range(n-1, -1, -1):
        if a[i] <= i+1:
            return i+2
    return 1


for t in range(0, int(input())):
    print(solve())