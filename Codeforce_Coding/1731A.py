def solve():
    n = int(input())
    a = list(map(int, input().split()))
    pro = 1
    flag = 0
    for ele in a:
        if ele >1:
            pro *= ele
        else:
            flag = 1

    if flag == 0:
        pro += 2020

    return 2022*pro


for t in range(0, int(input())):
    print(solve())