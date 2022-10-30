def solve():
    n = int(input())
    a = list(map(int, input().split()))

    a.sort()
    v1 = 0
    v2 = 0
    for i in range(n - 1, 1, -1):
        v1 = max(2 *(a[i]) - a[i - 1] - a[0], v1)
    for i in range(0, n - 2):
        v2 = max(a[i + 1] + a[-1] - 2 * a[i], v2)
    return max(v1, v2)


for t in range(0, int(input())):
    print(solve())