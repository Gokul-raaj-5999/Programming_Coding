for i in range(0, int(input())):
    a,b,c = str(input()).split(' ')
    if int(a) + int(b) >= 10 or int(b) + int(c) >= 10 or int(c) + int(a) >= 10:
        print('YES')
    else:
        print('NO')
