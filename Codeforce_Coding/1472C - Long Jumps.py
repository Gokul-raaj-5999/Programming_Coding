for t in range(int(input())): #back tracking in dp
    n=int(input())
    a=list(map(int,input().split()))
    for i in range(n-1,-1,-1):
        if i+a[i]<n:
            a[i]+=a[i+a[i]]
            
    print(max(a))


"""def solve():  # normal solution top down approch
    count = 0
    n = int(input())
    a = list(map(int, input().split()))
    b = []

    for i in range(0, n):
        count = 0
        if i + a[i] > n-1:
            b.append(a[i])
            continue
        ini = i + a[i]
        count += a[i]
        while ini <= n-1:
            count += a[ini]
            ini = ini + a[ini]
                    
        b.append(count)
    # print(b)
    return max(b)


for t in range(0, int(input())):
    print(solve())
    # print()"""


