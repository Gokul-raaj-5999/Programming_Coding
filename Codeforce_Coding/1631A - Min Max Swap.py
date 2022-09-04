for _ in range(0, int(input())):
    n = int(input())
    ar = list(map(int, input().split()))
    br = list(map(int, input().split()))
    
    for i in range(0, n):
        if(ar[i] > br[i]):
            ar[i], br[i] = br[i], ar[i]
    m = max(ar)*max(br)
    print(m)


"""
A. Min Max Swap
time limit per test1 second
memory limit per test256 megabytes
inputstandard input
outputstandard output
You are given two arrays a and b of n positive integers each. You can apply the following operation to them any number of times:

Select an index i (1≤i≤n) and swap ai with bi (i. e. ai becomes bi and vice versa).
Find the minimum possible value of max(a1,a2,…,an)⋅max(b1,b2,…,bn) you can get after applying such operation any number of times (possibly zero).

Input
The input consists of multiple test cases. The first line contains a single integer t (1≤t≤100) — the number of test cases. Description of the test cases follows.

The first line of each test case contains an integer n (1≤n≤100) — the length of the arrays.

The second line of each test case contains n integers a1,a2,…,an (1≤ai≤10000) where ai is the i-th element of the array a.

The third line of each test case contains n integers b1,b2,…,bn (1≤bi≤10000) where bi is the i-th element of the array b.

Output
For each test case, print a single integer, the minimum possible value of max(a1,a2,…,an)⋅max(b1,b2,…,bn) you can get after applying such operation any number of times.

Example
inputCopy
3
6
1 2 6 5 1 2
3 4 3 2 2 5
3
3 3 3
3 3 3
2
1 2
2 1
outputCopy
18
9
2
Note
In the first test, you can apply the operations at indices 2 and 6, then a=[1,4,6,5,1,5] and b=[3,2,3,2,2,2], max(1,4,6,5,1,5)⋅max(3,2,3,2,2,2)=6⋅3=18.

In the second test, no matter how you apply the operations, a=[3,3,3] and b=[3,3,3] will always hold, so the answer is max(3,3,3)⋅max(3,3,3)=3⋅3=9.

In the third test, you can apply the operation at index 1, then a=[2,2], b=[1,1], so the answer is max(2,2)⋅max(1,1)=2⋅1=2.

"""
