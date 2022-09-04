def diss(x , y, sx, sy):
    dis = abs(x-sx) + abs(y-sy)
    return int(dis)

def rbcall(n, m, sx, sy, d):
    for i in range(1, n+1):
        if diss(i, 1, sx, sy) <= d:
            return 1
    for i in range(1, m+1):
        if diss(n, i, sx, sy) <= d:
            return 1
    return 2   

def ulcall(n, m, sx, sy, d):
    for i in range(1, m+1):
        # print('       ', 1, i)
        # print(diss(1, i, sx, sy), d)
        if diss(1, i, sx, sy) <= d:
            return 1
    for i in range(1, n+1):
        # print('       ', i, m)
        # print(diss(i, m, sx, sy), d)
        if diss(i, m, sx, sy) <= d:
            return 1
    return 2 



t = int(input())
for _ in range(0, t):
    n, m, sx, sy, d = list(map(int, input().split()))

    if rbcall(n, m, sx, sy, d) == 2:
        # print('rb', end = ' ')
        print(n+m-2)
    elif ulcall(n, m, sx, sy, d) == 2:
        # print('ul', end= ' ')
        print(n+m-2)
    else:
        print(-1)


"""
B. Deadly Laser
time limit per test2 seconds
memory limit per test256 megabytes
inputstandard input
outputstandard output
The robot is placed in the top left corner of a grid, consisting of n rows and m columns, in a cell (1,1).

In one step, it can move into a cell, adjacent by a side to the current one:

(x,y)→(x,y+1);
(x,y)→(x+1,y);
(x,y)→(x,y−1);
(x,y)→(x−1,y).
The robot can't move outside the grid.

The cell (sx,sy) contains a deadly laser. If the robot comes into some cell that has distance less than or equal to d to the laser, it gets evaporated. The distance between two cells (x1,y1) and (x2,y2) is |x1−x2|+|y1−y2|.

Print the smallest number of steps that the robot can take to reach the cell (n,m) without getting evaporated or moving outside the grid. If it's not possible to reach the cell (n,m), print -1.

The laser is neither in the starting cell, nor in the ending cell. The starting cell always has distance greater than d to the laser.

Input
The first line contains a single integer t (1≤t≤104) — the number of testcases.

The only line of each testcase contains five integers n,m,sx,sy,d (2≤n,m≤1000; 1≤sx≤n; 1≤sy≤m; 0≤d≤n+m) — the size of the grid, the cell that contains the laser and the evaporating distance of the laser.

The laser is neither in the starting cell, nor in the ending cell ((sx,sy)≠(1,1) and (sx,sy)≠(n,m)). The starting cell (1,1) always has distance greater than d to the laser (|sx−1|+|sy−1|>d).

Output
For each testcase, print a single integer. If it's possible to reach the cell (n,m) from (1,1) without getting evaporated or moving outside the grid, then print the smallest amount of steps it can take the robot to reach it. Otherwise, print -1.

Example
inputCopy
3
2 3 1 3 0
2 3 1 3 1
5 5 3 4 1
outputCopy
3
-1
8
"""
