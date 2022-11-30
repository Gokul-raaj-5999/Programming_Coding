def solve():
    n = int(input())
    arr = list(map(int, input().split()))

    arr.sort()
    for i in range(0, n-2):
        a ,b, c = arr[i], arr[i+1], arr[i+2]
        if a < b+c and b < c+a and c < a+b:
            return 'Yes'
    return 'No'

print ( solve() )