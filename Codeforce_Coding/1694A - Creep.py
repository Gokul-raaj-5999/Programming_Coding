for t in range(0, int(input())):
    z, o = map(int, input().split())
    s = ''
    while z and o:
        s += '01'
        z -= 1
        o -= 1

    s += '1'*o
    s += '0'*z
    print(s)
