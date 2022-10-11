def solve():
    n = int(input())
    a = []
    for i in range(0, n):
        a.append(i+1)
    mid = n//2
    if n%2 != 0:
        mid += 1

    aa = a[:mid]
    bb = a[mid:]
    # print(aa, bb)
    bb.reverse()
    bb.extend(aa)

    # print(bb)
    flag = 0
    for i in range(0, n):
        if bb[i] == i+1:
            flag = 1
            break
  
    if flag or n == 3:
        print(-1)
    else:
        print(' '.join(str(x) for x in bb))


for t in range(0, int(input())):
    solve()