for t in range(0, int(input())):
    n = int(input())
    b = list(map(int, input().split()))
    b.sort()

    flag = 0
    for i in range(0, n-1):
        if b[i] == b[i+1]:
            flag = 1
            break
        

    if flag:
        print('YES')
    else:
        print('NO')
    
"""
B. Valerii Against Everyone
time limit per test1 second
memory limit per test256 megabytes
inputstandard input
outputstandard output
You're given an array b of length n. Let's define another array a, also of length n, for which ai=2bi (1≤i≤n).

Valerii says that every two non-intersecting subarrays of a have different sums of elements. You want to determine if he is wrong. More formally, you need to determine if there exist four integers l1,r1,l2,r2 that satisfy the following conditions:

1≤l1≤r1<l2≤r2≤n;
al1+al1+1+…+ar1−1+ar1=al2+al2+1+…+ar2−1+ar2.
If such four integers exist, you will prove Valerii wrong. Do they exist?

An array c is a subarray of an array d if c can be obtained from d by deletion of several (possibly, zero or all) elements from the beginning and several (possibly, zero or all) elements from the end.

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1≤t≤100). Description of the test cases follows.

The first line of every test case contains a single integer n (2≤n≤1000).

The second line of every test case contains n integers b1,b2,…,bn (0≤bi≤109).

Output
For every test case, if there exist two non-intersecting subarrays in a that have the same sum, output YES on a separate line. Otherwise, output NO on a separate line.

Also, note that each letter can be in any case.

Example
inputCopy
2
6
4 3 0 1 2 0
2
2 5
outputCopy
YES
NO
Note
In the first case, a=[16,8,1,2,4,1]. Choosing l1=1, r1=1, l2=2 and r2=6 works because 16=(8+1+2+4+1).

In the second case, you can verify that there is no way to select to such subarrays.

"""