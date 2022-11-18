def solve():
    n = int(input())
    if n == 1:
        return -1
    s = '2'+ '3'*(n-1)

    return int(s)


for t in range(0, int(input())):
    print ( solve() )