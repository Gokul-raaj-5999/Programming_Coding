def solve():
    n = int(input())
    a = list(map(int, input().split()))
    eve =0
    odd =0
    for i in a:
        if i%2 == 0:
            eve += i
        else:
            odd += i
    if eve> odd:
        return 'Yes'
    else:
        return 'No'



for t in range(0, int(input())):
    print(solve())