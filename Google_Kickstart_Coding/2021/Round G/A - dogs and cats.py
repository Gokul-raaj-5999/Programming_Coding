def call(n,d,c,m,s):
    if(n*'C' == s):
        return("YES")

    for i in s:
        if(i=="D"):
            if(d<=0 or c<0):
                return("NO")
            d-=1
            c+=m
        else:
            c-=1
    return("YES")
    

for case in range(int(input())):
    n, d, c, m = (int(i) for i in input().split())
    s = str(input())
    ans = call(n,d,c,m,s)
    print(f"Case #{case+1}: {ans}")
    
