def rotate(A):
    N = len(A[0])
    for i in range(N // 2):
        for j in range(i, N - i - 1):
            temp = A[i][j]
            A[i][j] = A[N - 1 - j][i]
            A[N - 1 - j][i] = A[N - 1 - i][N - 1 - j]
            A[N - 1 - i][N - 1 - j] = A[j][N - 1 - i]
            A[j][N - 1 - i] = temp
    return A

def check(a):
    if a[0][0] < a[0][1] and a[1][0] < a[1][1] and a[0][0] < a[1][0] and a[0][1] < a[1][1]:
        return 1
    else:
        return 0
def solve():
    a = []
    for i in range(2):
        a.append(list(map(int, input().split())))

    if check(a):
        return 'Yes'
    for i in range(4):
        a = rotate(a)
        if check(a):
            return 'Yes'
    return 'No'

for t in range(0, int(input())):
    print( solve() ) 
