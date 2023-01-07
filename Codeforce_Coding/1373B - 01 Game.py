for t in range(0, int(input())):
    s = input()
    zc = s.count('0')
    oc = s.count('1')

    m = min(zc, oc)
    if m > 0:
        if m%2 == 0:
            print('NET')
        else:
            print('DA')
    else:
        print('NET')