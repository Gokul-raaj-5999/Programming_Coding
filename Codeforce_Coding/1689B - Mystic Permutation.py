t = int(input())
for _ in range(0, t):
    n = int(input())
    a = list(map(int, input().split()))
    b = []

    for i in range(1, n+1):
        b.append(i)
    
    if n == 1:
        b = [-1]
    else:
        for i in range(0, n-1):
            if a[i] == b[i]:
                b[i], b[i+1] = b[i+1], b[i]

        if a[n-1] == b[n-1]:
            b[n-2], b[n-1] = b[n-1], b[n-2]

    print(' '.join(str(x) for x in b))


"""
B. Mystic Permutation
time limit per test2 seconds
memory limit per test256 megabytes
inputstandard input
outputstandard output
Monocarp is a little boy who lives in Byteland and he loves programming.

Recently, he found a permutation of length n. He has to come up with a mystic permutation. It has to be a new permutation such that it differs from the old one in each position.

More formally, if the old permutation is p1,p2,…,pn and the new one is q1,q2,…,qn it must hold that
p1≠q1,p2≠q2,…,pn≠qn.
Monocarp is afraid of lexicographically large permutations. Can you please help him to find the lexicographically minimal mystic permutation?

Input
There are several test cases in the input data. The first line contains a single integer t (1≤t≤200) — the number of test cases. This is followed by the test cases description.

The first line of each test case contains a positive integer n (1≤n≤1000) — the length of the permutation.

The second line of each test case contains n distinct positive integers p1,p2,…,pn (1≤pi≤n). It's guaranteed that p is a permutation, i. e. pi≠pj for all i≠j.

It is guaranteed that the sum of n does not exceed 1000 over all test cases.

Output
For each test case, output n positive integers — the lexicographically minimal mystic permutations. If such a permutation does not exist, output −1 instead.

Example
inputCopy
4
3
1 2 3
5
2 3 4 5 1
4
2 3 1 4
1
1
outputCopy
2 3 1
1 2 3 4 5
1 2 4 3
-1
Note
In the first test case possible permutations that are mystic are [2,3,1] and [3,1,2]. Lexicographically smaller of the two is [2,3,1].

In the second test case, [1,2,3,4,5] is the lexicographically minimal permutation and it is also mystic.

In third test case possible mystic permutations are [1,2,4,3], [1,4,2,3], [1,4,3,2], [3,1,4,2], [3,2,4,1], [3,4,2,1], [4,1,2,3], [4,1,3,2] and [4,3,2,1]. The smallest one is [1,2,4,3].
"""
