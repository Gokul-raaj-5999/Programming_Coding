def solve():
    n = int(input())
    s = input()

    dic = {}
    for i in range(0, n-1):
        t = s[i:i+2]
        if t in dic:
            if dic[t] < i-1:
                return 'Yes'

        else:
            dic[t] = i
    return 'No'

    

for t in range(0, int(input())):
    print(solve()) #single varialbe return 

"""
B. Notepad#
time limit per test3 seconds
memory limit per test256 megabytes
inputstandard input
outputstandard output
You want to type the string s, consisting of n lowercase Latin letters, using your favorite text editor Notepad#.

Notepad# supports two kinds of operations:

append any letter to the end of the string;
copy a continuous substring of an already typed string and paste this substring to the end of the string.
Can you type string s in strictly less than n operations?

Input
The first line contains a single integer t (1≤t≤104) — the number of testcases.

The first line of each testcase contains a single integer n (1≤n≤2⋅105) — the length of the string s.

The second line contains a string s, consisting of n lowercase Latin letters.

The sum of n doesn't exceed 2⋅105 over all testcases.

Output
For each testcase, print "YES" if you can type string s in strictly less than n operations. Otherwise, print "NO".

Example
inputCopy
6
10
codeforces
8
labacaba
5
uohhh
16
isthissuffixtree
1
x
4
momo
outputCopy
NO
YES
NO
YES
NO
YES
Note
In the first testcase, you can start with typing "codef" (5 operations), then copy "o" (1 operation) from an already typed part, then finish with typing "rces" (4 operations). That will be 10 operations, which is not strictly less than n. There exist other ways to type "codeforces". However, no matter what you do, you can't do less than n operations.

In the second testcase, you can type "labac" (5 operations), then copy "aba" (1 operation), finishing the string in 6 operations.

"""