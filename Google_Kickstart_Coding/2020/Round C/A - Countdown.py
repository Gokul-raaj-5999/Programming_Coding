def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a = a[::-1]
    count = 0
    i = 0
    f = 0
    while i < n-1:
        if a[i] == 1:
            f = 1
        # print(a[i], f , count)
        if f == 1 and a[i]+1 == a[i+1] and a[i] < k:
            f = 1
            if f == 1 and a[i+1] == k:
                count += 1
                f = 0
        else:
            if f == 1 and a[i] == k:
                count += 1
            f = 0
        # print(a[i], f, count)
        # print()
        i += 1
    
    return count


for t in range(0, int(input())):
    print(f'Case #{t+1}: {solve()}')


"""
Problem
Avery has an array of N positive integers. The i-th integer of the array is Ai.

A contiguous subarray is an m-countdown if it is of length m and contains the integers m, m-1, m-2, ..., 2, 1 in that order. For example, [3, 2, 1] is a 3-countdown.

Can you help Avery count the number of K-countdowns in her array?

Input
The first line of the input gives the number of test cases, T. T test cases follow. Each test case begins with a line containing the integers N and K. The second line contains N integers. The i-th integer is Ai.

Output
For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the number of K-countdowns in her array.

Limits
Time limit: 20 seconds.
Memory limit: 1 GB.
1 ≤ T ≤ 100.
2 ≤ K ≤ N.
1 ≤ Ai ≤ 2 × 105, for all i.
Test Set 1
2 ≤ N ≤ 1000.
Test Set 2
2 ≤ N ≤ 2 × 105 for at most 10 test cases.
For the remaining cases, 2 ≤ N ≤ 1000.
Sample
Sample Input
save_alt
content_copy
3
12 3
1 2 3 7 9 3 2 1 8 3 2 1
4 2
101 100 99 98
9 6
100 7 6 5 4 3 2 1 100
Sample Output
save_alt
content_copy
Case #1: 2
Case #2: 0
Case #3: 1
In sample case #1, there are two 3-countdowns as highlighted below.

1 2 3 7 9 3 2 1 8 3 2 1
1 2 3 7 9 3 2 1 8 3 2 1
In sample case #2, there are no 2-countdowns.

In sample case #3, there is one 6-countdown as highlighted below.

100 7 6 5 4 3 2 1 100"""