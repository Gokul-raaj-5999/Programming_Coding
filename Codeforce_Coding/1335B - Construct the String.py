import math

def solve():
    n, a, b = list(map(int, input().split()))
    rep = ''
    for i in range(0, b):
        rep += chr(97+i)

    mul = (n//b)+1
    op = rep*mul
    op = op[:n]
    return op
    

for t in range(0, int(input())):
    print(solve())