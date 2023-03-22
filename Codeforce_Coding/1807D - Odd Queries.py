# for codeforce use fast io

def solve():
    n ,q = map(int,input().split())
    arr = list(map(int,input().split()))
    sarr = [0]
    for i in arr:
        sarr.append(sarr[-1] + i)
    sarr.pop(0)
    # print(sarr)
    tsum = sarr[-1]
    
    for i in range(0, q):
        tsum = sarr[-1]
        l,r, k = list(map(int, input().split()))
        sumx = k*(r-l+1)
        if l == 1:
            tsum -= (sarr[r-1])
        else:
            tsum -= (sarr[r-1] - sarr[l-1-1])
        tsum += sumx
        # print(tsum, sumx)
        if tsum % 2 != 0:
            print('YES')
        else:
            print('NO')


    

for t in range(0, int(input())):
    solve()