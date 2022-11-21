def check(arr):
    a = 0
    ans = 0
    for i in range(len(arr)-1, -1, -1):
        if arr[i] == 0:
            a += 1
        else:
            ans += a
    return ans

def solve():
    n = int(input())
    s = list(map(int, input().split()))

    init = check(s)
    cas1 = s.copy()
    cas2 = s.copy()

    for i in range(n-1, -1, -1):
        if cas1[i] == 1:
            cas1[i] = 0
            break
    for i in range(n):
        if cas2[i] == 0:
            cas2[i] = 1
            break
    return max(init, check(cas1), check(cas2))




for t in range(0, int(input())):
    print ( solve())


"""
E. Binary Inversions
time limit per test2 seconds
memory limit per test256 megabytes
inputstandard input
outputstandard output
You are given a binary array† of length n. You are allowed to perform one operation on it at most once. In an operation, you can choose any element and flip it: turn a 0 into a 1 or vice-versa.

What is the maximum number of inversions‡ the array can have after performing at most one operation?

† A binary array is an array that contains only zeroes and ones.

‡ The number of inversions in an array is the number of pairs of indices i,j such that i<j and ai>aj.

Input
The input consists of multiple test cases. The first line contains an integer t (1≤t≤104) — the number of test cases. The description of the test cases follows.

The first line of each test case contains an integer n (1≤n≤2⋅105) — the length of the array.

The following line contains n space-separated positive integers a1, a2,..., an (0≤ai≤1) — the elements of the array.

It is guaranteed that the sum of n over all test cases does not exceed 2⋅105.

Output
For each test case, output a single integer  — the maximum number of inversions the array can have after performing at most one operation.

Example
inputCopy
5
4
1 0 1 0
6
0 1 0 0 1 0
2
0 0
8
1 0 1 1 0 0 0 1
3
1 1 1
outputCopy
3
7
1
13
2
Note
For the first test case, the inversions are initially formed by the pairs of indices (1,2), (1,4), (3,4), being a total of 3, which already is the maximum possible.

For the second test case, the inversions are initially formed by the pairs of indices (2,3), (2,4), (2,6), (5,6), being a total of four. But, by flipping the first element, the array becomes 1,1,0,0,1,0, which has the inversions formed by the pairs of indices (1,3), (1,4), (1,6), (2,3), (2,4), (2,6), (5,6) which total to 7 inversions which is the maximum possible.

"""