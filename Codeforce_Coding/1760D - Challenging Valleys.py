def solve():
    n = int(input())
    a = list(map(int, input().split()))
    if n == 1:
        return 'YES'

    f = 0
    for i in range(0, n-1):
        if a[i] <= a[i+1]:
            f = 1
        else:
            f = 0
            break
    if f:
        return 'YES'
    
    f = 0
    for i in range(0, n-1):
        if a[i] >= a[i+1]:
            f = 1
        else:
            f = 0
            break
    if f:
        return 'YES'
    
    f = 1
    for i in range(0, n-1):
        if a[i] >= a[i+1] and f == 1:
            f = 1
            continue
        else:
            f = 2
        
        if f == 2 and a[i] <= a[i+1]:
            f == 2
            continue
        else:
            f = -1
            break

    if f == 2:
        return 'YES'
    return 'NO'
        

    



for t in range(0, int(input())):
    print(solve())