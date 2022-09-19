def solve():
    n = int(input())
    ada = []
    cha = []
    for i in range(0, n):
        c, d, id = list(map(str, input().split()))
        ada.append([c, int(id)])
        cha.append([int(d), int(id)])
    # print(ada, cha)
    ada.sort()
    cha.sort()
    count = 0
    for i in range(0, n):
        if ada[i][1] == cha[i][1]:
            count += 1
    return count

for t in range(0, int(input())):
    print(f'Case #{t+1}: {solve()}')