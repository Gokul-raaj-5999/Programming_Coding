for t in range(0, int(input())):
    n  = int(input())
    count = 0
    inc = 0
    while n > 9:
        inc = n//10
        n = n%10 + inc
        count += (inc*10)
    count += n
    print(count)
