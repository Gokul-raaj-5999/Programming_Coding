def solve():
    n = int(input())
    s = input()
    eve = set()
    odd = set()
    if n == 1:
        return 'Yes'
    for i in range(0, n):
        if i%2 ==0:
            eve.add(s[i])
        else:
            odd.add(s[i])

    x = eve & odd
    if len(x) > 0:
        return 'No'
    return 'Yes'




for t in range(0, int(input())):
    print(solve())