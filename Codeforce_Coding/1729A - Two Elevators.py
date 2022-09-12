def solve():
    a, b, c = list(map(int, input().split()))
    f = a
    s = c + abs( b - c )
    if f == s:
        return 3
    elif f < s:
        return 1
    else:
        return 2


    return 

for t in range(0, int(input())):
    ans = solve()
    print (ans)
    # print()



"""
3
1 2 3
3 1 2
3 2 1


"""