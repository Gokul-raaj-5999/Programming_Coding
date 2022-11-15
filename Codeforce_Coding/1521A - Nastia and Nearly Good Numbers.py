def solve():
    a, b = map(int, input().split())
    if b == 1:
        print('NO')
    else:
        print('YES')
        print(a, a*b, a*(b+1))


for t in range(0, int(input())):
    solve()