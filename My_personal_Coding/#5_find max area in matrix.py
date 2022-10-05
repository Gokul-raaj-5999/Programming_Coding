def maxHist(row):
    result = []
    top_val = 0
    max_area = 0
    area = 0 
    i = 0
    while (i < len(row)):
        if (len(result) == 0) or (row[result[-1]] <= row[i]):
            result.append(i)
            i += 1
        else:
            top_val = row[result.pop()]
            area = top_val * i

            if (len(result)):
                area = top_val * (i - result[-1] - 1)
            max_area = max(area, max_area)

    while (len(result)):
        top_val = row[result.pop()]
        area = top_val * i
        if (len(result)):
            area = top_val * (i - result[-1] - 1)

        max_area = max(area, max_area)

    return max_area

def maxRectangle(A):
    result = maxHist(A[0])
    for i in range(1, len(A)):
        for j in range(len(A[i])):
            if (A[i][j]):
                A[i][j] += A[i - 1][j]
        result = max(result, maxHist(A[i]))

    return result


n = int(input())
mat = []
for i in range(0, n):
    mat.append([0]*n)
for i in mat:
    print(i)
print()
a, b , c, d = list(map(int, input().split()))
for i in range(a, c+1):
    for j in range(b, d+1):
        mat[i][j] = 1

for i in mat:
    print(i)

area = maxRectangle(mat)
print(area)

