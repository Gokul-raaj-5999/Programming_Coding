for t in range(int(input())):
    n, m, r, c = map(int, input().split())
    a = [list(input()) for i in range(n)]
    if "B" not in str(a):
        print(-1)
        continue
    print(2 - ("B" in a[r-1] + list([*zip(*a)][c-1])) - (a[r-1][c-1] == 'B'))

"""
A. Not Shading
time limit per test1 second
memory limit per test256 megabytes
inputstandard input
outputstandard output
There is a grid with n rows and m columns. Some cells are colored black, and the rest of the cells are colored white.

In one operation, you can select some black cell and do exactly one of the following:

color all cells in its row black, or
color all cells in its column black.
You are given two integers r and c. Find the minimum number of operations required to make the cell in row r and column c black, or determine that it is impossible.

Input
The input consists of multiple test cases. The first line contains an integer t (1≤t≤100) — the number of test cases. The description of the test cases follows.

The first line of each test case contains four integers n, m, r, and c (1≤n,m≤50; 1≤r≤n; 1≤c≤m) — the number of rows and the number of columns in the grid, and the row and column of the cell you need to turn black, respectively.

Then n lines follow, each containing m characters. Each of these characters is either 'B' or 'W' — a black and a white cell, respectively.

Output
For each test case, if it is impossible to make the cell in row r and column c black, output −1.

Otherwise, output a single integer — the minimum number of operations required to make the cell in row r and column c black.

Example
inputCopy
9
3 5 1 4
WBWWW
BBBWB
WWBBB
4 3 2 1
BWW
BBW
WBB
WWB
2 3 2 2
WWW
WWW
2 2 1 1
WW
WB
5 9 5 9
WWWWWWWWW
WBWBWBBBW
WBBBWWBWW
WBWBWBBBW
WWWWWWWWW
1 1 1 1
B
1 1 1 1
W
1 2 1 1
WB
2 1 1 1
W
B
outputCopy
1
0
-1
2
2
0
-1
1
1
Note
The first test case is pictured below.


We can take the black cell in row 1 and column 2, and make all cells in its row black. Therefore, the cell in row 1 and column 4 will become black.


In the second test case, the cell in row 2 and column 1 is already black.

In the third test case, it is impossible to make the cell in row 2 and column 2 black.

The fourth test case is pictured below.


We can take the black cell in row 2 and column 2 and make its column black.


Then, we can take the black cell in row 1 and column 2 and make its row black.


Therefore, the cell in row 1 and column 1 will become black.

"""
