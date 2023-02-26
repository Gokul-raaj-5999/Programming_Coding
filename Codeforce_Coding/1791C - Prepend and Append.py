def solve():
    n = int(input())
    s = input()

    i, j = 0,n-1
    while (i< j):
        if (s[i]=='0' and s[j]=='1') or (s[i]=='1' and s[j]=='0'):
            i += 1
            j -=1
        else:
            return s[i:j+1]
    return s[i:j+1]
for t in range(0, int(input())):
    print(len(solve()))