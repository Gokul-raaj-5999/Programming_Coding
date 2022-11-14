def check(s):
    dic = [0]*10
    for ele in s:
        n = int(ele)
        dic[n] += 1
    dictinc = set()
    for i in s:
        dictinc.add(i)
    l = len(dictinc)
    for i in dic:
        if i > 0  and i != l:
            return False
    print('re -> T')
    return True

    
    


def solve():
    n = int(input())
    s = input()

    a = set()
    count = 0
    for i in range(0, n):
        for j in range(i,n):
            ss = s[i:j+1]
            if check(ss):
                count += 1
            a.add(ss)
        

    print(count)
    print(a)



for t in range(0, int(input())):
    solve()
    print()