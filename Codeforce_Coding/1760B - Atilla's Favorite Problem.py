def solve():
    n = int(input())
    s = input()
    m = 0

    for i in s:
        x = ord(i)-96
        m = max(m, x)

    print(m)

for t in range(0, int(input())):
    solve()