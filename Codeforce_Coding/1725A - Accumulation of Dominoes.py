n, m = map(int, input().split())
count = 0
if m == 1 and n == 1:
    count = 0
elif m == 1 and n >= 2:
    count += (n-1)*m
else:
    count += (m-1)*n
print(count)
    

"""
A. Accumulation of Dominoes
time limit per test1 second
memory limit per test256 megabytes
inputstandard input
outputstandard output
Pak Chanek has a grid that has N rows and M columns. Each row is numbered from 1 to N from top to bottom. Each column is numbered from 1 to M from left to right.

Each tile in the grid contains a number. The numbers are arranged as follows:

Row 1 contains integers from 1 to M from left to right.
Row 2 contains integers from M+1 to 2×M from left to right.
Row 3 contains integers from 2×M+1 to 3×M from left to right.
And so on until row N.
A domino is defined as two different tiles in the grid that touch by their sides. A domino is said to be tight if and only if the two numbers in the domino have a difference of exactly 1. Count the number of distinct tight dominoes in the grid.

Two dominoes are said to be distinct if and only if there exists at least one tile that is in one domino, but not in the other.

Input
The only line contains two integers N and M (1≤N,M≤109) — the number of rows and columns in the grid.

Output
An integer representing the number of distinct tight dominoes in the grid.

Examples
inputCopy
3 4
outputCopy
9
inputCopy
2 1
outputCopy
1
Note
The picture below is the grid that Pak Chanek has in the first example.


The picture below is an example of a tight domino in the grid.

"""