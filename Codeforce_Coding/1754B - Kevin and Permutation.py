for _ in range(0, int(input())):
    n = int(input())
    a = []
    b = []
    c = []
    for i in range(1, n//2+1):
        a.append(i)
    for i in range(n//2+1, n+1):
        b.append(i)
    # print(a, b)
    for i in range(0, max(len(a), len(b))):
        if i < len(b):
            c.append(b[i])
        if i < len(a):
            c.append(a[i])
    print(*c)
        



"""
B. Kevin and Permutation
time limit per test1 second
memory limit per test256 megabytes
inputstandard input
outputstandard output
For his birthday, Kevin received the set of pairwise distinct numbers 1,2,3,…,n as a gift.

He is going to arrange these numbers in a way such that the minimum absolute difference between two consecutive numbers be maximum possible. More formally, if he arranges numbers in order p1,p2,…,pn, he wants to maximize the value
mini=1n−1|pi+1−pi|,
where |x| denotes the absolute value of x.

Help Kevin to do that.

Input
Each test consists of multiple test cases. The first line contains a single integer t (1≤t≤100) — the number of test cases. Description of the test cases follows.

The only line of each test case contains an integer n (2≤n≤1000) — the size of the set.

Output
For each test case print a single line containing n distinct integers p1,p2,…,pn (1≤pi≤n) describing the arrangement that maximizes the minimum absolute difference of consecutive elements.

Formally, you have to print a permutation p which maximizes the value mini=1n−1|pi+1−pi|.

If there are multiple optimal solutions, print any of them.

Example
inputCopy
2
4
3
outputCopy
2 4 1 3
1 2 3
Note
In the first test case the minimum absolute difference of consecutive elements equals min{|4−2|,|1−4|,|3−1|}=min{2,3,2}=2. It's easy to prove that this answer is optimal.

In the second test case each permutation of numbers 1,2,3 is an optimal answer. The minimum absolute difference of consecutive elements equals to 1.

"""