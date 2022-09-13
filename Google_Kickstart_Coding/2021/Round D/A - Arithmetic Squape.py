import math


def solve():
    a1 ,a2, a3 = list(map(int, input().split()))
    b1, b3 = list(map(int, input().split()))
    c1, c2, c3 = list(map(int, input().split()))

    com = 0
    if math.ceil((a1 + a3)/2) == a2 and math.floor((a1 + a3)/2) == a2:
        com += 1
    if math.ceil((c1 + c3)/2) == c2 and math.floor((c1 + c3)/2) == c2:
        com += 1
    if math.ceil((a1 + c1)/2) == b1 and math.floor((a1 + c1)/2) == b1:
        com += 1
    if int(math.ceil((a3 + c3)/2)) == b3 and int(math.floor((a3 + c3)/2)) == b3:
        com += 1

    dic = {}
    if int((a2+c2)//2) == int(math.ceil((a2+c2)/2)): 
        x = (a2+c2)//2
        if x in dic:
            dic[x] += 1
        else:
            dic[x] = 1
    if int((b1+b3)//2) == int(math.ceil((b1+b3)/2)):
        x = (b1+b3)//2
        if x in dic:
            dic[x] += 1
        else:
            dic[x] = 1
    if int((a1+c3)//2) == int(math.ceil((a1+c3)/2)):
        x = (a1+c3)//2
        if x in dic:
            dic[x] += 1
        else:
            dic[x] = 1
    if int((c1+a3)//2) == int(math.ceil((c1+a3)/2)):
        x = (c1+a3)//2
        if x in dic:
            dic[x] += 1
        else:
            dic[x] = 1

    m = 0
    for i in dic:
        if m < dic[i]:
            m = dic[i]
    return com+ m
    


for t in range(0, int(input())):
    a = solve()
    print(f"Case #{t+1}:", end= ' ')
    print(a)




""""
3
3 4 11
10 9
-1 6 7
4 1 6
3 5
2 5 6
9 9 9
9 9
9 9 9

"""