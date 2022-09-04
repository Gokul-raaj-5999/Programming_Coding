for _ in range(0, int(input())):
    n = int(input())
    ar = list(map(int, input().split()))
    codd = 0
    ceve = 0
    for i in ar:
        if i%2 == 0:
            ceve+=1
        else:
            codd+=1
    # print(ceve, codd)
    if codd == n or ceve == n:
        print(0)
    else:
        print(min(codd, ceve))


"""
A. Beat The Odds
time limit per test1 second
memory limit per test256 megabytes
inputstandard input
outputstandard output
Given a sequence a1,a2,…,an, find the minimum number of elements to remove from the sequence such that after the removal, the sum of every 2 consecutive elements is even.

Input
Each test contains multiple test cases. The first line contains a single integer t (1≤t≤100) — the number of test cases. Description of the test cases follows.

The first line of each test case contains a single integer n (3≤n≤105).

The second line of each test case contains n integers a1,a2,…,an (1≤ai≤109) — elements of the sequence.

It is guaranteed that the sum of n over all test cases does not exceed 105.

Output
For each test case, print a single integer — the minimum number of elements to remove from the sequence such that the sum of every 2 consecutive elements is even.

Example
inputCopy
2
5
2 4 3 6 8
6
3 5 9 7 1 3
outputCopy
1
0
Note
In the first test case, after removing 3, the sequence becomes [2,4,6,8]. The pairs of consecutive elements are {[2,4],[4,6],[6,8]}. Each consecutive pair has an even sum now. Hence, we only need to remove 1 element to satisfy the condition asked.

In the second test case, each consecutive pair already has an even sum so we need not remove any element.

"""
