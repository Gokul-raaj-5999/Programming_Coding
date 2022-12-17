def solve():
    n = int(input())
    s = input()
    ss = ''
    a = []
    for i in s:
        a.append(int(i))
    
    sum = a[0]
    for i in range(1, n):
        if sum == 1 and a[i] == 1:
            ss += '-'
            sum = 0
        elif sum == 1 and a[i] == 0:
            ss += '-'
            sum = 1
        elif sum == 0 and a[i] == 1:
            ss += '+'
            sum = 1
        elif sum == 0 and a[i] == 0:
            ss += '+'
            sum = 0
    
    return ss

for t in range(0, int(input())):
    print(solve())