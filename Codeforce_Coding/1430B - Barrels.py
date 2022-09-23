def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    a.sort()
    a = a[::-1]
    if len(a) > 2:
        i = 1
        while a[i] > 0 and k > 0 and i < len(a):
            a[0] += a[i]
            a[i] = 0
            i += 1
            k -= 1
            # print(a)
            if i == len(a):
                break
        return(max(a) - min(a))
    elif len(a) == 2:
        if a[1] > 0:
            a[0] += a[1]
            a[1] = 0
        return(max(a) - min(a))



for t in range(0, int(input())):
    print(solve())




"""
B. Barrels
time limit per test2 seconds
memory limit per test256 megabytes
inputstandard input
outputstandard output
You have n barrels lined up in a row, numbered from left to right from one. Initially, the i-th barrel contains ai liters of water.

You can pour water from one barrel to another. In one act of pouring, you can choose two different barrels x and y (the x-th barrel shouldn't be empty) and pour any possible amount of water from barrel x to barrel y (possibly, all water). You may assume that barrels have infinite capacity, so you can pour any amount of water in each of them.

Calculate the maximum possible difference between the maximum and the minimum amount of water in the barrels, if you can pour water at most k times.

Some examples:

if you have four barrels, each containing 5 liters of water, and k=1, you may pour 5 liters from the second barrel into the fourth, so the amounts of water in the barrels are [5,0,5,10], and the difference between the maximum and the minimum is 10;
if all barrels are empty, you can't make any operation, so the difference between the maximum and the minimum amount is still 0.
Input
The first line contains one integer t (1≤t≤1000) — the number of test cases.

The first line of each test case contains two integers n and k (1≤k<n≤2⋅105) — the number of barrels and the number of pourings you can make.

The second line contains n integers a1,a2,…,an (0≤ai≤109), where ai is the initial amount of water the i-th barrel has.

It's guaranteed that the total sum of n over test cases doesn't exceed 2⋅105.

Output
For each test case, print the maximum possible difference between the maximum and the minimum amount of water in the barrels, if you can pour water at most k times.

Example
inputCopy
2
4 1
5 5 5 5
3 2
0 0 0
outputCopy
10
0
"""