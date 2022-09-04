for _ in range(0, int(input())):
    n, m = map(int, input().split())
    
    if n>1 and m>1:
        spaces = n*(m-1) + m*(n-1)
    else:
        spaces = n*m
    shape = n*m
    
    if(spaces == shape):
        print('YES')
    else:
        print('NO')

"""
A. Puzzle Pieces
time limit per test1 second
memory limit per test256 megabytes
inputstandard input
outputstandard output
You are given a special jigsaw puzzle consisting of n⋅m identical pieces. Every piece has three tabs and one blank, as pictured below.


The jigsaw puzzle is considered solved if the following conditions hold:

The pieces are arranged into a grid with n rows and m columns.
For any two pieces that share an edge in the grid, a tab of one piece fits perfectly into a blank of the other piece.
Through rotation and translation of the pieces, determine if it is possible to solve the jigsaw puzzle.

Input
The test consists of multiple test cases. The first line contains a single integer t (1≤t≤1000) — the number of test cases. Next t lines contain descriptions of test cases.

Each test case contains two integers n and m (1≤n,m≤105).

Output
For each test case output a single line containing "YES" if it is possible to solve the jigsaw puzzle, or "NO" otherwise. You can print each letter in any case (upper or lower).

Example
inputCopy
3
1 3
100000 100000
2 2
outputCopy
YES
NO
YES
Note
For the first test case, this is an example solution:


For the second test case, we can show that no solution exists.

For the third test case, this is an example solution:


"""
