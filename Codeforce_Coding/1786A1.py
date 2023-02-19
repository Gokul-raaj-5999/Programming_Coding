def solve():
    n = int(input())
    ala = bob = 0

    i =1
    sum = 0
    count = 0
    while sum <= n:
        if count %2 ==  0:
            ala += i
            count +=  1
        else:
            bob += i
            count += 1
        sum += i
        i += 1
        print(ala, bob)






for t in range(0, int(input())):
    solve()
    print()