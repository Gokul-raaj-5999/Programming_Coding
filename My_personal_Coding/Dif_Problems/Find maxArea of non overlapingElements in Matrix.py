"""
this problem is not finished 
"""

def maxarea(vec):    
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

    for i in vec:
        print(i)
    area = maxRectangle(vec)
    return(area)


def verticalfindmatsize(mat, pos, n):
    xpos, ypos = pos
    xc, yc = 0, 0
    unset = set()
    unlst = list()
    vec = []
    for i in range(0, n):
        vec.append([0]*n)

    i, j = xpos, ypos
    for j in range(ypos ,n):
        for i in range(xpos, n):
            unlst.append(mat[i][j])
            unset.add(mat[i][j])
            if len(unlst) != len(unset):
                print(unlst[:-1])
                # print(xpos, ypos, i, j)
                a = maxarea(vec)
                print()
                return (a)
            else:
                vec[i][j] = 1
            ipre = i
            jpre = j
    print(unlst)
    # print(xpos, ypos, i, j)
    a = maxarea(vec)
    print()
    return (a)
      
def horizontalfindmatsize(mat, pos, n):
    xpos, ypos = pos
    xc, yc = 0, 0
    unset = set()
    unlst = list()
    vec = []
    for i in range(0, n):
        vec.append([0]*n)

    i, j = xpos, ypos
    for i in range(xpos ,n):
        for j in range(ypos, n):
            unlst.append(mat[i][j])
            unset.add(mat[i][j])
            if len(unlst) != len(unset):
                print(unlst[:-1])
                # print(xpos, ypos, i, j)
                a = maxarea(vec)
                print()
                return (a)
            else:
                vec[i][j] = 1
            ipre = i
            jpre = j
    print(unlst)
    # print(xpos, ypos, i, j)
    a = maxarea(vec)
    print()
    return (a)


for t in range(0, int(input())):
    print('-------------------------------')
    n = int(input())
    mat = []
    for _ in range(0, n):
        mat.append(list(map(int, input().split())))
    # print(mat)
    pos = [0,0]
    areav, areah = [], []

    for x in range(0 ,n):
        for y in range(0, n):
            pos = [x,y]
            areav.append(verticalfindmatsize(mat, pos, n))
            areah.append(horizontalfindmatsize(mat, pos, n))
    
    print(areav, areah)
    print(max(areav), max(areah))
    