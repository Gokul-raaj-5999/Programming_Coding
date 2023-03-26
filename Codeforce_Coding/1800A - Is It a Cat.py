def solve():
    n = int(input())
    s = input().lower()
    con = ['m', 'e', 'o' ,'w']

    op = []
    if n < 4:
        return 'No'
    
    op.append(s[0])
    for i in range(1, n):
        if op[-1] == s[i]:
            continue
        elif s[i] in con:
            op.append(s[i])
        else:
            return 'No'
    if op == con:
        return 'Yes'
    return 'No'
     


for t in range(0, int(input())):
    print(solve())