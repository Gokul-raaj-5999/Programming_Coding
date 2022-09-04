for _ in range(0, int(input())):
    n = int(input())
    px,nx,py,ny,ori = [0],[0],[0],[0],[]
    
    for i in range(0, n):
        x,y = map(int, input().split())
        if x>0 and y==0:
            px.append(x)
        elif x<0 and y==0:
            nx.append(abs(x))
        elif x==0 and y>0:
            py.append(y)
        elif x==0 and y<0:
            ny.append(abs(y))
        elif x==0 and y==0:
            ori.append(1)
            
    # print(px,py,nx,ny,ori)
    mpx, mpy, mnx, mny = max(px), max(py), max(nx), max(ny)
    dis = mpx + mpy + mpx + mnx + mpy + mny + mnx + mny
    print(dis)


"""
A. Traveling Salesman Problem
time limit per test1 second
memory limit per test256 megabytes
inputstandard input
outputstandard output
You are living on an infinite plane with the Cartesian coordinate system on it. In one move you can go to any of the four adjacent points (left, right, up, down).

More formally, if you are standing at the point (x,y), you can:

go left, and move to (x−1,y), or
go right, and move to (x+1,y), or
go up, and move to (x,y+1), or
go down, and move to (x,y−1).
There are n boxes on this plane. The i-th box has coordinates (xi,yi). It is guaranteed that the boxes are either on the x-axis or the y-axis. That is, either xi=0 or yi=0.

You can collect a box if you and the box are at the same point. Find the minimum number of moves you have to perform to collect all of these boxes if you have to start and finish at the point (0,0).

Input
The first line contains a single integer t (1≤t≤100) — the number of test cases.

The first line of each test case contains a single integer n (1≤n≤100) — the number of boxes.

The i-th line of the following n lines contains two integers xi and yi (−100≤xi,yi≤100) — the coordinate of the i-th box. It is guaranteed that either xi=0 or yi=0.

Do note that the sum of n over all test cases is not bounded.

Output
For each test case output a single integer — the minimum number of moves required.

Example
inputCopy
3
4
0 -2
1 0
-1 0
0 2
3
0 2
-3 0
0 -1
1
0 0
outputCopy
12
12
0
Note
In the first test case, a possible sequence of moves that uses the minimum number of moves required is shown below.


(0,0)→(1,0)→(1,1)→(1,2)→(0,2)→(−1,2)→(−1,1)→(−1,0)→(−1,−1)→(−1,−2)→(0,−2)→(0,−1)→(0,0)
In the second test case, a possible sequence of moves that uses the minimum number of moves required is shown below.


(0,0)→(0,1)→(0,2)→(−1,2)→(−2,2)→(−3,2)→(−3,1)→(−3,0)→(−3,−1)→(−2,−1)→(−1,−1)→(0,−1)→(0,0)
In the third test case, we can collect all boxes without making any moves.

"""
