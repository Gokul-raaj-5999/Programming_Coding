import math

def solve():
    n = int(input())

    for i in range(2, 30):
        ans = (2**i)-1
        if n%ans == 0:
            return n//ans

for t in range(0, int(input())):
    print(solve())