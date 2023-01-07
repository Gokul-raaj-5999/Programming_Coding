import math

def solve():
    h, n, m = list(map(int, input().split()))
    ch = h
    
    i = 0
    while i < n and h > 0:
        h = math.floor(h/2)+10
        i += 1

    if h <= 0:
        return 'YES'

    h = h - 10*m
    if h <= 0:
        return 'YES'

    #----- checking the reverse case
    h = ch
    h = h - 10*m
    if h <= 0:
        return 'YES'
    i = 0
    while i < n and h > 0:
        h = math.floor(h/2)+10
        i += 1

    if h <= 0:
        return 'YES'

    return 'NO'



for t in range(0, int(input())):
    print(solve())