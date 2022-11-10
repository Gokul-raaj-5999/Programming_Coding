import math

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    g = a[0]

    for i in range(1, len(a)):
        g = math.gcd(g, a[i])


    if g == 1:
        return (0)
    elif math.gcd(g, n) == 1:
        return(1)
    elif len(a) > 1 and math.gcd(g, n-1) == 1 :
        return(2)
    else:
        return(3)


for t in range(0, int(input())):
    print( solve() )