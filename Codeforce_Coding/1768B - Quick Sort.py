def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    cv = 1
    for i in range(0, n):
        if a[i] == cv:
            cv += 1
    
    return ((n-cv+k)//k)

    


for t in range(0, int(input())):
    print(solve())