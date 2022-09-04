def fact(n):
    p = 0
    for i in range(1, n+1):
        p+=i
    return p


n = int(input())
if n == 1:
    print(1)
elif n == 2:
    print(5)
else:
    fn = fact(n)
    sum = fn + 2*(fn-n) + ((fn-n)-(n-1))
    print(sum)

"""
A. Alex and a Rhombus
time limit per test1 second
memory limit per test256 megabytes
inputstandard input
outputstandard output
While playing with geometric figures Alex has accidentally invented a concept of a n-th order rhombus in a cell grid.

A 1-st order rhombus is just a square 1×1 (i.e just a cell).

A n-th order rhombus for all n≥2 one obtains from a n−1-th order rhombus adding all cells which have a common side with it to it (look at the picture to understand it better).


Alex asks you to compute the number of cells in a n-th order rhombus.

Input
The first and only input line contains integer n (1≤n≤100) — order of a rhombus whose numbers of cells should be computed.

Output
Print exactly one integer — the number of cells in a n-th order rhombus.

Examples
inputCopy
1
outputCopy
1
inputCopy
2
outputCopy
5
inputCopy
3
outputCopy
13
Note
Images of rhombus corresponding to the examples are given in the statement.
"""
