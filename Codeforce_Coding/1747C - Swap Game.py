def solve():
    n = int(input())
    a = list(map(int, input().split()))
    f = 1
    x = a[0]
    y = min(a[1:])
    if x <= y:
        print('Bob')
    else:
        print('Alice')
    

for t in range(0, int(input())):
    solve()

