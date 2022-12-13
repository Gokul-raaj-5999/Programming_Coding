
def solve():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    m1 = a.count(min(a))
    m2 = a.count(max(a))
    if min(a) == max(a):
        sum = n*(n-1)
    else:
        sum = (m1*m2)*2
    print(sum)
     

for t in range(0, int(input())):
    solve()
