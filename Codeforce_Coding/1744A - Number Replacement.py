def solve():
    n = int(input())
    a = list(map(int, input().split()))
    s = input()
    lst = [[]]*(max(a))
    # print(lst)

    for i in range(0, n):
        ele = s[i]
        num = a[i] -1

        if lst[num] == []:
            lst[num] = [ele]
        else:
            if lst[num] != [ele]:
                return 'No'
    # print(lst)
    return 'Yes'





for _ in range(0, int(input())):
    print(solve())