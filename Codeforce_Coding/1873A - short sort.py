for i in range(0, int(input())):
    a,b,c = str(input())
    count = 0
    if a == 'a':
        count += 1
    if b == 'b':
        count += 1
    if c == 'c':
        count += 1
    if count >= 1:
        print('YES')
    else:
        print('NO')