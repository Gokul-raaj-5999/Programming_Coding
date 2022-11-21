def solve():
    a = list(map(int, input().split()))
    a.sort()
    print(a[1])


for t in range(0, int(input())):
    solve()