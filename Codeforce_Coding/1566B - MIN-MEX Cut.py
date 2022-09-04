t = int(input())
for test in range(t):
    s = input()
    zeroes = s.count('0')
    if zeroes == 0:
        print(0)
        continue

    first = s.find('0')
    last = s.rfind('0')
    if last - first + 1 == zeroes:
        print(1)
    else:
        print(2)


"""
B. MIN-MEX Cut
time limit per test1 second
memory limit per test256 megabytes
inputstandard input
outputstandard output
A binary string is a string that consists of characters 0 and 1.

Let MEX of a binary string be the smallest digit among 0, 1, or 2 that does not occur in the string. For example, MEX of 001011 is 2, because 0 and 1 occur in the string at least once, MEX of 1111 is 0, because 0 and 2 do not occur in the string and 0<2.

A binary string s is given. You should cut it into any number of substrings such that each character is in exactly one substring. It is possible to cut the string into a single substring — the whole string.

A string a is a substring of a string b if a can be obtained from b by deletion of several (possibly, zero or all) characters from the beginning and several (possibly, zero or all) characters from the end.

What is the minimal sum of MEX of all substrings pieces can be?

Input
The input consists of multiple test cases. The first line contains a single integer t (1≤t≤104) — the number of test cases. Description of the test cases follows.

Each test case contains a single binary string s (1≤|s|≤105).

It's guaranteed that the sum of lengths of s over all test cases does not exceed 105.

Output
For each test case print a single integer — the minimal sum of MEX of all substrings that it is possible to get by cutting s optimally.

Example
inputCopy
6
01
1111
01100
101
0000
01010
outputCopy
1
0
2
1
1
2
Note
In the first test case the minimal sum is MEX(0)+MEX(1)=1+0=1.

In the second test case the minimal sum is MEX(1111)=0.

In the third test case the minimal sum is MEX(01100)=2.

"""
