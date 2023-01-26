import math

def solve():
    n = int(input())
    a = list(map(int, input().split()))

    a.sort()
    ocount = 0
    for i in a:
        if i == 1:
            ocount += 1

    rem = len(a) - ocount

    # print(ocount//2, rem) 
    sum = math.ceil(ocount/2) + rem
    return sum


for t in range(0, int(input())):
    print(solve())