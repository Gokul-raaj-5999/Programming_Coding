for _ in range(0, int(input())):
    spa = input()
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    f = list(map(int, input().split()))
    ans = abs(a[0] - b[0]) + abs(a[1] - b[1])
    if ((a[0] == b[0] and a[0] == f[0] and min(a[1], b[1]) < f[1] and f[1] < max(a[1], b[1])) or (a[1] == b[1] and a[1] == f[1] and min(a[0], b[0]) < f[0] and f[0] < max(a[0], b[0]))):
        ans += 2
    print(ans)


"""
A. Shortest Path with Obstacle
time limit per test2 seconds
memory limit per test512 megabytes
inputstandard input
outputstandard output
There are three cells on an infinite 2-dimensional grid, labeled A, B, and F. Find the length of the shortest path from A to B if:

in one move you can go to any of the four adjacent cells sharing a side;
visiting the cell F is forbidden (it is an obstacle).
Input
The first line contains an integer t (1≤t≤104) — the number of test cases in the input. Then t test cases follow. Before each test case, there is an empty line.

Each test case contains three lines. The first one contains two integers xA,yA (1≤xA,yA≤1000) — coordinates of the start cell A. The second one contains two integers xB,yB (1≤xB,yB≤1000) — coordinates of the finish cell B. The third one contains two integers xF,yF (1≤xF,yF≤1000) — coordinates of the forbidden cell F. All cells are distinct.

Coordinate x corresponds to the column number and coordinate y corresponds to the row number (see the pictures below).

Output
Output t lines. The i-th line should contain the answer for the i-th test case: the length of the shortest path from the cell A to the cell B if the cell F is not allowed to be visited.

Example
inputCopy
7

1 1
3 3
2 2

2 5
2 1
2 3

1000 42
1000 1
1000 1000

1 10
3 10
2 10

3 8
7 8
3 7

2 1
4 1
1 1

1 344
1 10
1 1
outputCopy
4
6
41
4
4
2
334
Note
An example of a possible shortest path for the first test case.
An example of a possible shortest path for the second test case.
"""
