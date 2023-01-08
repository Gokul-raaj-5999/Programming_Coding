def solve():
    x = int(input())
    ans = []
    sum = 0
    last = 9
    while sum < x and last > 0:
        ans.append(min(x-sum, last))
        sum += last
        last -= 1

    if sum < x:
        return -1
    ans = ans[::-1]
    return ''.join(str(x) for x in ans)

for t in range(0, int(input())):
    print(solve())