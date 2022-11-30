def solve():
    a,b,n, s = list(map(int, input().split()))

    tot_a = a*n
    tot_b = b*1

    # if tot_a <= s:
    #     rem = s - tot_a
    #     if b >= rem:
    #         return 'Yes'
    #     else:
    #         return 'No'
    # else:
    x = s//n 
    # print(x)
    if x <= a:
        rem = s - x*n
        if b >= rem:
            return 'Yes'
        else:
            return 'No'
    else:
        rem = s - n*a
        if b >= rem:
            return 'Yes'
        else:
            return 'No'

for t in range(0, int(input())):
    print( solve())