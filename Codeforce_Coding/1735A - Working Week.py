import math

def solve():
    n = int(input())
    if n <= 8:
        return 0
    else:
        p3 = n
        avg = n//3
        p1 = 2
        x = (p3+p1)//2
        p2 = p1 + avg

        d1 = p1
        d2 = p2-p1
        d3 = p3-p2
        # print(p1,p2,p3)
        # print(d1,d2,d3)
        # print( abs(d1-d2), abs(d2-d3), abs(d3-d1))

    return min(abs(d1-d2), abs(d2-d3), abs(d3-d1))

for t in range(0, int(input())):
    print(solve())
    # print()