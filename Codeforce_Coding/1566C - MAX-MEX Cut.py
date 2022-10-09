def solve():
    n = int(input())
    ar = list(map(int, input()))
    br = list(map(int, input()))
    # print(ar, br)

    count = 0
    i = 0
    while i < n:
        if ar[i] != br[i]:
            count += 2
            i += 1
        elif ar[i] == br[i] and i < n-1 and ar[i+1] == br[i+1] and ar[i] != ar[i+1] :
            count += 2
            i += 2
        elif ar[i] == br[i] == 1:
            count += 0
            i += 1
        elif ar[i] == br[i] == 0:
            count += 1
            i += 1
        # print(count, end=' ')
    
    return count

for t in range(0, int(input())):
    print(solve())


"""
C. MAX-MEX Cut
time limit per test1 second
memory limit per test256 megabytes
inputstandard input
outputstandard output
A binary string is a string that consists of characters 0 and 1. A bi-table is a table that has exactly two rows of equal length, each being a binary string.

Let MEX of a bi-table be the smallest digit among 0, 1, or 2 that does not occur in the bi-table. For example, MEX for [00111010] is 2, because 0 and 1 occur in the bi-table at least once. MEX for [111111] is 0, because 0 and 2 do not occur in the bi-table, and 0<2.

You are given a bi-table with n columns. You should cut it into any number of bi-tables (each consisting of consecutive columns) so that each column is in exactly one bi-table. It is possible to cut the bi-table into a single bi-table — the whole bi-table.

What is the maximal sum of MEX of all resulting bi-tables can be?

Input
The input consists of multiple test cases. The first line contains a single integer t (1≤t≤104) — the number of test cases. Description of the test cases follows.

The first line of the description of each test case contains a single integer n (1≤n≤105) — the number of columns in the bi-table.

Each of the next two lines contains a binary string of length n — the rows of the bi-table.

It's guaranteed that the sum of n over all test cases does not exceed 105.

Output
For each test case print a single integer — the maximal sum of MEX of all bi-tables that it is possible to get by cutting the given bi-table optimally.

Example
inputCopy
4
7
0101000
1101100
5
01100
10101
2
01
01
6
000000
111111
outputCopy
8
8
2
12
Note
In the first test case you can cut the bi-table as follows:

[01], its MEX is 2.
[1010], its MEX is 2.
[11], its MEX is 0.
[01], its MEX is 2.
[00], its MEX is 1.
[00], its MEX is 1.
The sum of MEX is 8."""