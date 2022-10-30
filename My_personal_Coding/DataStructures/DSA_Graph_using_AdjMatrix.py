"""
undirected graph using adjecent matrix
"""

def matprint(mat):
    for i in mat:
        print(i)
    print()


if __name__ == '__main__':
    n, m = map(int, input().split())
    adjmat = [[0 for i in range(0, n)] for j in range(0, m)]

    matprint(adjmat)

    for i in range(int(input())):
        u, v = map(int, input().split())
        adjmat[u][v] = 1
        adjmat[v][u] = 1

    matprint(adjmat)

    

"""
i/p

5 5
6
0 1
1 2
2 3
3 4
4 0
1 4

"""