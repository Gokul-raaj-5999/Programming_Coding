def solve():
    n,m = map(int,input().split())
    count,r = 0, m/n
    for i in [2, 3]:
        while r%i == 0:
            count += 1
            r/= i
    return count if r == 1 else -1
    

print(solve())