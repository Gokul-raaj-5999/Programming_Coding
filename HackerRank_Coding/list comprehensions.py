if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
temp=[0,0,0]
final=list()
for a in range(0,x+1,1):
    for b in range(0,y+1,1):
        for c in range(0,z+1,1):
            sum=a+b+c
            temp=[a,b,c]
            if(sum!=n):
                final.append(temp)
print(final)

#############################################################################
"""
SAMPLE1:
    INPUT:
        1
        1
        1
        2
    OUTPUT:
        [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]

SAMPLE2:
    INPUT:
        2
        2
        2
        2
    OUTPUT:
        [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 2], [0, 2, 1], [0, 2, 2],
        [1, 0, 0], [1, 0, 2], [1, 1, 1], [1, 1, 2], [1, 2, 0], [1, 2, 1],
        [1, 2, 2], [2, 0, 1], [2, 0, 2], [2, 1, 0], [2, 1, 1], [2, 1, 2],
        [2, 2, 0], [2, 2, 1], [2, 2, 2]]
"""
