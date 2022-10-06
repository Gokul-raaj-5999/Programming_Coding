def solve():
    n, m = map(int, input().split())
    print(n//2+1, m//2+1)


for t in range(0, int(input())):
    solve()



"""
A. Immobile Knight
time limit per test2 seconds
memory limit per test256 megabytes
inputstandard input
outputstandard output
There is a chess board of size n×m. The rows are numbered from 1 to n, the columns are numbered from 1 to m.

Let's call a cell isolated if a knight placed in that cell can't move to any other cell on the board. Recall that a chess knight moves two cells in one direction and one cell in a perpendicular direction:


Find any isolated cell on the board. If there are no such cells, print any cell on the board.

Input
The first line contains a single integer t (1≤t≤64) — the number of testcases.

The only line of each testcase contains two integers n and m (1≤n,m≤8) — the number of rows and columns of the board.

Output
For each testcase, print two integers — the row and the column of any isolated cell on the board. If there are no such cells, print any cell on the board.

Example
inputCopy
3
1 7
8 8
3 3
outputCopy
1 7
7 2
2 2
Note
In the first testcase, all cells are isolated. A knight can't move from any cell of the board to any other one. Thus, any cell on board is a correct answer.

In the second testcase, there are no isolated cells. On a normal chess board, a knight has at least two moves from any cell. Thus, again, any cell is a correct answer.

In the third testcase, only the middle cell of the board is isolated. The knight can move freely around the border of the board, but can't escape the middle.


"""