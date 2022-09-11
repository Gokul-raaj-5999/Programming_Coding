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
     

def zerocase(vec):
    chan = 1
    while chan > 0:
        chan = 0
        for i in range(0, len(vec)-1):
            if vec[i] == 0 and vec[i+1] > 0:
                vec[i], vec[i+1] = vec[i+1], vec[i]
                chan += 1
    return vec

def move(n, a):
    for i in range(0, n):
        vec = a[i]
        vec = vec[::-1]
        pos = 0
        while pos < len(vec)-1:
            if vec[pos] == vec[pos+1]:
                vec[pos+1] = vec[pos] + vec[pos+1] 
                vec[pos] = 0
                pos += 2
            elif vec[pos] == 0 and vec[pos+1] > 0:
                pos += 1
            elif vec[pos] > 0 and vec[pos+1] == 0:
                vec[pos], vec[pos+1] = vec[pos+1], vec[pos]
                pos += 1
            else:
                pos += 1
        vec = zerocase(vec)
        a[i] = vec[::-1]
    return a
            

def solve():
    n, cond = input().split()
    n = int(n)
    a = []
    for i in range(0, n):
        a.append(list(map(int, input().split())))
    
    if cond == 'right':
        a = move(n, a)
        return a

    elif cond == 'up':
        a = rotate(a)
        a = move(n, a)
        a = rotate(a)
        a = rotate(a)
        a = rotate(a)
        return a

    elif cond == 'left':
        a = rotate(a)
        a = rotate(a)
        a = move(n, a)
        a = rotate(a)
        a = rotate(a)
        return a      

    elif cond == 'down':
        a = rotate(a)
        a = rotate(a)
        a = rotate(a)
        a = move(n, a)
        a = rotate(a)
        return a
        


for t in range(0, int(input())):
    ans = solve()
    print(f"Case #{t+1}:")
    for i in range(0, len(ans)):
        print(' '.join(str(x) for x in ans[i]))

"""
3
4 right
2 0 2 4
2 0 4 2
2 2 4 8
2 2 4 4
10 up
2 0 0 0 0 0 0 0 0 0
2 0 0 0 0 0 0 0 0 0
2 0 0 0 0 0 0 0 0 0
2 0 0 0 0 0 0 0 0 0
2 0 0 0 0 0 0 0 0 0
2 0 0 0 0 0 0 0 0 0
2 0 0 0 0 0 0 0 0 0
2 0 0 0 0 0 0 0 0 0
2 0 0 0 0 0 0 0 0 0
2 0 0 0 0 0 0 0 0 0
3 right
2 2 2
4 4 4
8 8 8

"""