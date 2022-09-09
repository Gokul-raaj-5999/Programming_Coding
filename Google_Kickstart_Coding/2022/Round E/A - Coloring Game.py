for t in range(0, int(input())):
    n = int(input())
    i = 1
    pos = 0
    bot = 0
    joo = 0
    while(i < n+1):
        if pos == 0:
            i+=2
            pos = 1
            bot+= 1
        else:
            i+=3
            pos = 0
            joo+=1
    print(f'Case #{t+1}: {bot}')