import math

def solve():
    n, m = map(int, input().split())
    print(math.ceil((math.ceil(n/m)*m)/n))
     

for t in range(0, int(input())):
    solve() 

