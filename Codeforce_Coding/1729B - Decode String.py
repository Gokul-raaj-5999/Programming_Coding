from re import sub
import string
from turtle import st



def solve():
    alp = list(string.ascii_lowercase)
    # print(alp)

    n = int(input())
    s = input()
    b = list(s)
    b = b[::-1]

    i = 0
    op = ''
    while i < n:
        if b[i] == '0':
            sub = int( (b[i+1]+b[i+2])[::-1])
            # print(sub)
            op += str(alp[sub-1])
            i+= 3
        else:
            sub = int(b[i])
            # print(sub)
            op += str(alp[sub-1])
            i += 1

    return op[::-1]


for t in range(0, int(input())):
    ans = solve()
    print(ans)
    # print()

"""
9
6
315045
4
1100
7
1213121
6
120120
18
315045615018035190
7
1111110
7
1111100
5
11111
4
2606

"""