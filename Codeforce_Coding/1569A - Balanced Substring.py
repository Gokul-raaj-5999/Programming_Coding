for _ in range(int(input())):
	n = int(input())
	s = input()
	for i in range(n - 1):
		if s[i] != s[i + 1]:
			print(i + 1, i + 2)
			break
	else:
		print(-1, -1)

"""
A. Balanced Substring
time limit per test2 seconds
memory limit per test256 megabytes
inputstandard input
outputstandard output
You are given a string s, consisting of n letters, each letter is either 'a' or 'b'. The letters in the string are numbered from 1 to n.

s[l;r] is a continuous substring of letters from index l to r of the string inclusive.

A string is called balanced if the number of letters 'a' in it is equal to the number of letters 'b'. For example, strings "baba" and "aabbab" are balanced and strings "aaab" and "b" are not.

Find any non-empty balanced substring s[l;r] of string s. Print its l and r (1≤l≤r≤n). If there is no such substring, then print −1 −1.

Input
The first line contains a single integer t (1≤t≤1000) — the number of testcases.

Then the descriptions of t testcases follow.

The first line of the testcase contains a single integer n (1≤n≤50) — the length of the string.

The second line of the testcase contains a string s, consisting of n letters, each letter is either 'a' or 'b'.

Output
For each testcase print two integers. If there exists a non-empty balanced substring s[l;r], then print l r (1≤l≤r≤n). Otherwise, print −1 −1.

Example
inputCopy
4
1
a
6
abbaba
6
abbaba
9
babbabbaa
outputCopy
-1 -1
1 6
3 6
2 5
Note
In the first testcase there are no non-empty balanced subtrings.

In the second and third testcases there are multiple balanced substrings, including the entire string "abbaba" and substring "baba".

"
