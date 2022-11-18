def solve():
    s = input()
    n = len(s)
    a = ['Y', 'e', 's']
    
    if s[0] == 'Y':
        j = 0
        for i in range(0, n):
            if s[i] == a[j]:
                j += 1
                j = j%3
                continue
            else:
                return 'NO'
        return 'YES'
    elif s[0] == 'e':
        j = 1
        for i in range(0, n):
            if s[i] == a[j]:
                j += 1
                j = j%3
                continue
            else:
                return 'NO'
        return 'YES'
    elif s[0] == 's':
        j = 2
        for i in range(0, n):
            if s[i] == a[j]:
                j += 1
                j = j%3
                continue
            else:
                return 'NO'
        return 'YES'
    else:
        return 'NO'
        


for t in range(0, int(input())):
    print(solve())