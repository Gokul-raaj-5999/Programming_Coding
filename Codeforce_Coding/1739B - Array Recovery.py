def solve():
    n = int(input())
    d = list(map(int, input().split()))
    a = [0]*n
    a[0] = d[0]
    flag = 0

    for i in range(1, n):
        a[i] = a[i-1] + d[i]
        if a[i-1] >= d[i] and d[i] != 0:
            flag = 1
            break
    
    if flag:
        print(-1)
    else:
        print(' '.join(str(x) for x in a))



for t in range(0, int(input())):
    solve()


"""
B. Array Recovery
time limit per test2 seconds
memory limit per test256 megabytes
inputstandard input
outputstandard output
For an array of non-negative integers a of size n, we construct another array d as follows: d1=a1, di=|ai−ai−1| for 2≤i≤n.

Your task is to restore the array a from a given array d, or to report that there are multiple possible arrays.

Input
The first line contains a single integer t (1≤t≤100) — the number of test cases.

The first line of each test case contains one integer n (1≤n≤100) — the size of the arrays a and d.

The second line contains n integers d1,d2,…,dn (0≤di≤100) — the elements of the array d.

It can be shown that there always exists at least one suitable array a under these constraints.

Output
For each test case, print the elements of the array a, if there is only one possible array a. Otherwise, print −1.

Example
inputCopy
3
4
1 0 2 5
3
2 6 3
5
0 0 0 0 0
outputCopy
1 1 3 8
-1
0 0 0 0 0
Note
In the second example, there are two suitable arrays: [2,8,5] and [2,8,11].

"""