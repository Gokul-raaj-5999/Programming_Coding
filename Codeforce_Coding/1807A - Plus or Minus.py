for t in range(0, int(input())):
    a, b,c = list(map(int, input().split()))
    if a-b == c:
        print('-')
    else:
        print('+')