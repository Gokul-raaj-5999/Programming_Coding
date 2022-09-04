for t in range(int(input())):
    n, k = map(int, input().split())
    s = input()
    rev = s[::-1]
    if k ==0:
        print(1)
    else:
        if s == rev:
            print(1)
        else:
            print(2)

"""
A. Reverse and Concatenate
time limit per test1 second
memory limit per test256 megabytes
inputstandard input
outputstandard output
Real stupidity beats artificial intelligence every time.
— Terry Pratchett, Hogfather, Discworld
You are given a string s of length n and a number k. Let's denote by rev(s) the reversed string s (i.e. rev(s)=snsn−1...s1). You can apply one of the two kinds of operations to the string:

replace the string s with s+rev(s)
replace the string s with rev(s)+s
How many different strings can you get as a result of performing exactly k operations (possibly of different kinds) on the original string s?

In this statement we denoted the concatenation of strings s and t as s+t. In other words, s+t=s1s2...snt1t2...tm, where n and m are the lengths of strings s and t respectively.

Input
The first line contains one integer t (1≤t≤100) — number of test cases. Next 2⋅t lines contain t test cases:

The first line of a test case contains two integers n and k (1≤n≤100, 0≤k≤1000) — the length of the string and the number of operations respectively.

The second string of a test case contains one string s of length n consisting of lowercase Latin letters.

Output
For each test case, print the answer (that is, the number of different strings that you can get after exactly k operations) on a separate line.

It can be shown that the answer does not exceed 109 under the given constraints.

Example
inputCopy
4
3 2
aab
3 3
aab
7 1
abacaba
2 0
ab
outputCopy
2
2
1
1
Note
In the first test case of the example:

After the first operation the string s can become either aabbaa or baaaab. After the second operation there are 2 possibilities for s: aabbaaaabbaa and baaaabbaaaab.

"""
