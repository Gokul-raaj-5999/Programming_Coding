from signal import set_wakeup_fd


def solve():
    n = int(input())
    a = []
    for i in range(1, n+1):
        a.append(i)
    s, e = a[:2]
    a1 = a[2:]
    ans = []
    ans.append(s)
    ans.extend(a1)
    ans.append(e)
    
    
    print(' '.join(str(x) for x in ans))

for t in range(0, int(input())):
    solve()


"""
B. Permutation Value
time limit per test2 seconds
memory limit per test512 megabytes
inputstandard input
outputstandard output
You are given an integer n. You have to construct a permutation of size n.

A permutation is an array where each integer from 1 to s (where s is the size of permutation) occurs exactly once. For example, [2,1,4,3] is a permutation of size 4; [1,2,4,5,3] is a permutation of size 5; [1,4,3] is not a permutation (the integer 2 is absent), [2,1,3,1] is not a permutation (the integer 1 appears twice).

A subsegment of a permutation is a contiguous subsequence of that permutation. For example, the permutation [2,1,4,3] has 10 subsegments: [2], [2,1], [2,1,4], [2,1,4,3], [1], [1,4], [1,4,3], [4], [4,3] and [3].

The value of the permutation is the number of its subsegments which are also permutations. For example, the value of [2,1,4,3] is 3 since the subsegments [2,1], [1] and [2,1,4,3] are permutations.

You have to construct a permutation of size n with minimum possible value among all permutations of size n.

Input
The first line contains one integer t (1≤t≤48) — the number of test cases.

Then, t lines follow. The i-th of them contains one integer n (3≤n≤50) representing the i-th test case.

Output
For each test case, print n integers — the permutation of size n with minimum possible value. If there are multiple such permutations, print any of them.

Example
inputCopy
2
5
6
outputCopy
1 4 3 5 2
4 1 6 2 5 3
Note
In the first example, the permutation [1,4,3,5,2] is one of the possible answers; its value is 2.

In the second example, the permutation [4,1,6,2,5,3] is one of the possible answers; its value is 2."""