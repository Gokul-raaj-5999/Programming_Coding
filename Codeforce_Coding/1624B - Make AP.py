def solve():
    a, b, c = list(map(int, input().split()))

    newa = b - (c-b)
    if newa >= a and newa%a == 0 and newa != 0:
        return 'YES'
    
    newb = a + (c -a)//2
    if newb >= b and (c-a)%2 == 0 and newb%b == 0 and newb != 0:
        return 'YES'
    
    newc = a + 2*(b-a)
    if newc >= c and newc%c == 0 and newc != 0:
        return 'YES'
    
    return 'NO'

    



for t in range(0, int(input())):
    print(solve())
    # print()



#make 3 munbres to a AP sequence.