def solve():
    n = int(input())
    a = []
    for i in range(0, n):
        x, y = list(map(int, input().split()))
        if x < y:
            x, y = y, x
        a.append([x,y])


    a.sort(reverse= True)
    # print(a)
    per = 0

    for x, y in a:
        per += 2*x + 2*y
    
    for i in range(len(a)-1, 0, -1):
        x,y = a[i]
        per -= 2*x

    return per


for t in range(0, int(input())):
    print(solve())