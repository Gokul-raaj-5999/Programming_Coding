t = int(input())
for test_case in range(t):
    n = int(input())
    int_list = list(map(int, input().split()))
    d = dict()
    for i in range(n):
        d[int_list[i]] = i + 1

    for i in range(n, 0, -1):
        print(d[i], end=" ")
    print()