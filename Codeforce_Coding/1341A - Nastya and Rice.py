for t in range(0, int(input())):
    n,a,b,c,d = list(map(int, input().split()))
    l = n*(a-b) 
    r = n*(a+b)
    if (r < (c-d)) or ((c+d) < l):
        print('No')
    else:
        print('Yes')