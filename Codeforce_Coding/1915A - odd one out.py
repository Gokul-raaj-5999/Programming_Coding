for i in range(0, int(input())):
    a,b,c = str(input()).split(' ')
    if a==b:
        print(c)
    elif b==c:
        print(a)
    else:
        print(b)