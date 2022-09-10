for _ in range(0, int(input())): 
    n = int(input())
    
    s = str(n)
    sum = 0
    for i in s:
        sum+= int(i)
    aele = str(9 - sum%9)
    if aele == '9':
        aele = '0'
    # print(aele)
    ans = 0

    if aele == '0':
        ans = int(s[0] + '0' + s[1:])
    else:
        flag = 1
        for i in range(0, len(s)):
            if int(s[i]) > int(aele):
                ans = int(s[:i] + aele + s[i:])
                flag = 0
                break

        if flag:
            ans = int(s + aele)


    # print(op)
    print(f'Case #{_+1}: {ans}')
        

"""
# time complexity O(n**2)
for _ in range(0, int(input())):
    n = int(input())
    
    s = str(n)
    sum = 0
    for i in s:
        sum+= int(i)
    aele = str(9 - sum%9)
    if aele == '9':
        aele = '0'
    # print(aele)
    op = []

    for i in range(0, len(s)+1):
        newele = s[:i] + aele + s[i:]
        if int(newele) % 9 == 0 and int(newele) != n:
            op.append(int(newele))

    # print(op)
    print(f'Case #{_+1}: {min(op)}')


input/ 

3
5
33
12121

"""