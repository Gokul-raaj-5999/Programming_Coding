import math

for t in range(0, int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    x = a[0]
    for i in range(1, n):
        x = math.gcd(x, a[i])
    print(int(a[n-1] / x))
