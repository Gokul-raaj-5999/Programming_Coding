for _ in range(0, int(input())):
    n = int(input())
    ar = list(map(int, input().split()))
    if( ar[-1] >= ar[0]+ar[1]):
        print(1,2,n)
    else:
        print(-1)
    


"""
A. Bad Triangle
time limit per test1 second
memory limit per test256 megabytes
inputstandard input
outputstandard output
You are given an array a1,a2,…,an, which is sorted in non-decreasing order (ai≤ai+1).

Find three indices i, j, k such that 1≤i<j<k≤n and it is impossible to construct a non-degenerate triangle (a triangle with nonzero area) having sides equal to ai, aj and ak (for example it is possible to construct a non-degenerate triangle with sides 3, 4 and 5 but impossible with sides 3, 4 and 7). If it is impossible to find such triple, report it.

Input
The first line contains one integer t (1≤t≤1000) — the number of test cases.

The first line of each test case contains one integer n (3≤n≤5⋅104) — the length of the array a.

The second line of each test case contains n integers a1,a2,…,an (1≤ai≤109; ai−1≤ai) — the array a.

It is guaranteed that the sum of n over all test cases does not exceed 105.

Output
For each test case print the answer to it in one line.

If there is a triple of indices i, j, k (i<j<k) such that it is impossible to construct a non-degenerate triangle having sides equal to ai, aj and ak, print that three indices in ascending order. If there are multiple answers, print any of them.

Otherwise, print -1.

Example
inputCopy
3
7
4 6 11 11 15 18 20
4
10 10 10 11
3
1 1 1000000000
outputCopy
2 3 6
-1
1 2 3
Note
In the first test case it is impossible with sides 6, 11 and 18. Note, that this is not the only correct answer.

In the second test case you always can construct a non-degenerate triangle.

"""
