n = int(input())
for i in range(n+1,10000):
    s = str(i)
    ar = []
    lst = []
    for ele in s:
        lst.append(ele)
    ar = list(set(lst))
    # print(ar)
    if(len(ar)==4):
        print(i)
        break