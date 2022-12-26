def check(lst, r):
    for i in lst:
        if i != r:
            return 0
    return 1


def solve():
    n = int(input())
    a = list(map(int, input().split()))

    zer = 0
    one = 0
    two = 0

    for i in a:
        if i%3 == 0:
            zer += 1
        elif i%3 == 1:
            one += 1
        else:
            two += 1
    # print(zer, one, two)
    r = n//3
    lst = [zer, one, two]
    count = 0
    i = 0
    while(1):
        if lst[i] > r:
            rem = lst[i] - r
            lst[i] -= rem
            count += rem
            if i == 2:
                i = -1
            lst[i+1] += rem
        # print(lst)
        if check(lst, r):
            break
        i += 1
                
        
    return count


for t in range(0, int(input())):
    print( solve() )