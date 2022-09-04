for _ in range(0, int(input())):
    n = int(input())
    
    if n %2 == 0:
        print(0, 0, n//2)
    else:
        print(-1)

"""
A. The Third Three Number Problem
time limit per test1 second
memory limit per test256 megabytes
inputstandard input
outputstandard output
You are given a positive integer n. Your task is to find any three integers a, b and c (0≤a,b,c≤109) for which (a⊕b)+(b⊕c)+(a⊕c)=n, or determine that there are no such integers.

Here a⊕b denotes the bitwise XOR of a and b. For example, 2⊕4=6 and 3⊕1=2.

Input
Each test contains multiple test cases. The first line contains a single integer t (1≤t≤104) — the number of test cases. The following lines contain the descriptions of the test cases.

The only line of each test case contains a single integer n (1≤n≤109).

Output
For each test case, print any three integers a, b and c (0≤a,b,c≤109) for which (a⊕b)+(b⊕c)+(a⊕c)=n. If no such integers exist, print −1.

Example
inputCopy
5
4
1
12
2046
194723326
outputCopy
3 3 1
-1
2 4 6
69 420 666
12345678 87654321 100000000
Note
In the first test case, a=3, b=3, c=1, so (3⊕3)+(3⊕1)+(3⊕1)=0+2+2=4.

In the second test case, there are no solutions.

In the third test case, (2⊕4)+(4⊕6)+(2⊕6)=6+2+4=12.
"""
