from math import gcd

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    count = 0
    for i in range(0, n):
        for j in range(i+1, n):
            if gcd(a[i],2*a[j]) > 1 or gcd(2*a[i],a[j]) > 1 :
                count += 1

    return count

for t in range(0, int(input())):
    print(solve())