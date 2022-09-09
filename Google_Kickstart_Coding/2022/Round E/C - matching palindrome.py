def getzarr(string):
    n = len(string)
    z = [0]*n
    l, r, k = 0, 0, 0
    for i in range(1, n):
        if i > r:
            l, r = i, i
            while r < n and string[r - l] == string[r]:
                r += 1
            z[i] = r - l
            r -= 1
        else:
            k = i - l
            if z[k] < r - i + 1:
                z[i] = z[k]
            else:
                l = i
                while r < n and string[r - l] == string[r]:
                    r += 1
                z[i] = r - l
                r -= 1
    return z


def solve():
    n = int(input())
    p = input()

    rev = p[::-1]
    str1 = p + '?' + rev
    str2 = rev + '?' + p
    vpref = getzarr(str1)
    vsufx = getzarr(str2)

    fnd = [False]*n
    for i in range(0, n):
        if vsufx[i] == n-i:
            fnd[i] = True
    minlen = n
    for i in range(0, n):
        if vpref[i] == n-i and fnd[n-i]:
            minlen = min(minlen, n-i)
    
    news = ''
    for i in range(1, minlen+1):
        news += p[i-1]
    
    return news[::-1]
        

for t in range(0, int(input())):
    ans = solve()
    print(f'Case #{t+1}: {ans}')



#tle in test case 2
"""
def solve():
    n = int(input())
    p = input()
    pos = 1

    while pos <= n:
        pref = p[:pos]
        suff = p[pos:]
        if pref == pref[::-1] and suff == suff[::-1]:
            return pref
        
        pos += 1



for t in range(0, int(input())):
    ans = solve()
    print(f'Case #{t+1}: {ans}')

"""