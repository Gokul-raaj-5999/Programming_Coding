def solve():
    n = int(input())
    a = list(map(int, input().split()))
    print(abs(sum(a)))

for t in range(0, int(input())):
    solve()