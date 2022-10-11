def solve():
    a, b = map(str, input().split())
    aa = 0
    bb = 0
    if a[-1] == 'S':
        for i in a:
            if i == 'X':
                aa -= 10
            if i == 'S':
                aa -= 1
    elif a[-1] == 'L':
        for i in a:
            if i == 'X':
                aa += 10
            if i == 'L':
                aa += 1
    else:
        aa = 0

    if b[-1] == 'S':
        for i in b:
            if i == 'X':
                bb -= 10
            if i == 'S':
                bb -= 1
    elif b[-1] == 'L':
        for i in b:
            if i == 'X':
                bb += 10
            if i == 'L':
                bb += 1
    else:
        bb = 0
    
    # print(aa, bb)
    if aa > bb:
        return '>'
    elif aa < bb:
        return '<'
    else:
        return '='

   
for t in range(0, int(input())):
    print(solve())