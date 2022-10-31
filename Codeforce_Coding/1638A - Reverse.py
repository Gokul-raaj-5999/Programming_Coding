for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    for j in range(n):
        if(a[j]!=j+1):
            b=a.index(j+1)
            z=a[j:b+1]
            a=a[:j]+z[::-1]+a[b+1:]
            break
    print(*a)