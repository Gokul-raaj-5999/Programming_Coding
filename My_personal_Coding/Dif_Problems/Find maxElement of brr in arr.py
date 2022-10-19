def solve(a,b):
    if len(a) < len(b): #b in a by default keep a as big
            a, b = b, a
    l1 = len(a)
    l2 = len(b)
    m = []
    
    i = 0
    j = 0
    while i < l1:
        j = 0
        if a[i] == b[j]:
            tem = []
            f = 1
            x = i
            j = 0
            print(x, j)
            while j < l2 and x < l1 and f:
                if a[x] == b[j]:
                    print(x, j)
                    tem.append(b[j])
                else:
                    f = 0 
                m.append(tem)
                print(m)
                j += 1
                x += 1
                                    
        i += 1
    print(m)
    ans = 0
    maxlen = 0
    for i in m:
        if len(i) > maxlen:
            maxlen = len(i)
            ans = i
    return ans

a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(solve(a,b))
            
            
        