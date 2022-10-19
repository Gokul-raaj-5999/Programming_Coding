for t in range(0, int(input())):
    s = list(map(int, input().split()))
    a=[1]*len(s)
    for i in range(len(s)-1):a[s[i]-1]=i+2
    print(*a)