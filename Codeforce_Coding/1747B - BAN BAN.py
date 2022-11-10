def solve():
    n = int(input())
    s = 'BAN'*n
    l = len(s)
    i = 0
    j = l//2
    op = []

    while i < j and j < l:
        if s[i] == 'B' and s[j] == 'N':
            op.append([i+1, j+1])
            i += 1
            j += 1
        elif s[i] == 'B' and s[j] != 'N':
            j += 1
        else:
            i+=1

    print(len(op))
    for i,j in op:
        print(i, j)

    


for t in range(0, int(input())):
    solve()



    """
    nind = []
    for i in range(len(s)//2, len(s)):
        if s[i] == 'N':
            nind.append(i)
    print(len(nind))
    oind = []
    for i in range(0, len(s)//2):
        if s[i]== 'B' or s[i] == 'A':
            oind.append(i)
    
    for i in range(0, len(nind)):
        print(oind[i]+1, nind[i]+1)"""