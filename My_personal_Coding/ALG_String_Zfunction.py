def zfunction1(string): # time complexity O(m+n)
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


def zfunction2(string): # time complexity O(n^2)
    n = len(string)
    z = [0]*n
    for i in range(1, n):
        while (i + z[i] < n and string[z[i]] == string[i+ z[i]] ):
            z[i] += 1
    return z


s = 'abacaba'
print(zfunction1(s))
print(zfunction2(s))
