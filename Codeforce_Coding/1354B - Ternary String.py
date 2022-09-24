def solve():
    s = list(input())
    m = 10**6
    l = [-1]*3
    for j in range(0, len(s)):
        l[int(s[j]) - 1] = j
        if l[0] >-1 and l[1] > -1 and l[2] > -1:
            m = min(m, max(l) - min(l) + 1)
    if m == 10**6:
        return 0
    else:
        return m

for t in range(0, int(input())):
    print(solve())
    # print()


"""
B. Ternary String
time limit per test2 seconds
memory limit per test256 megabytes
inputstandard input
outputstandard output
You are given a string s such that each its character is either 1, 2, or 3. You have to choose the shortest contiguous substring of s such that it contains each of these three characters at least once.

A contiguous substring of string s is a string that can be obtained from s by removing some (possibly zero) characters from the beginning of s and some (possibly zero) characters from the end of s.

Input
The first line contains one integer t (1≤t≤20000) — the number of test cases.

Each test case consists of one line containing the string s (1≤|s|≤200000). It is guaranteed that each character of s is either 1, 2, or 3.

The sum of lengths of all strings in all test cases does not exceed 200000.

Output
For each test case, print one integer — the length of the shortest contiguous substring of s containing all three types of characters at least once. If there is no such substring, print 0 instead.

Example
inputCopy
7
123
12222133333332
112233
332211
12121212
333333
31121
outputCopy
3
3
4
4
0
0
4
Note
Consider the example test:

In the first test case, the substring 123 can be used.

In the second test case, the substring 213 can be used.

In the third test case, the substring 1223 can be used.

In the fourth test case, the substring 3221 can be used.

In the fifth test case, there is no character 3 in s.

In the sixth test case, there is no character 1 in s.

In the seventh test case, the substring 3112 can be used.

"""