t = int(input())
for i in range(t):
    x, y = map(int, input().split())
    if y % x != 0:
        print(0, 0)
    else:
        print(1, y // x)


"""
A. Number Transformation
time limit per test2 seconds
memory limit per test512 megabytes
inputstandard input
outputstandard output
You are given two integers x and y. You want to choose two strictly positive (greater than zero) integers a and b, and then apply the following operation to x exactly a times: replace x with b⋅x.

You want to find two positive integers a and b such that x becomes equal to y after this process. If there are multiple possible pairs, you can choose any of them. If there is no such pair, report it.

For example:

if x=3 and y=75, you may choose a=2 and b=5, so that x becomes equal to 3⋅5⋅5=75;
if x=100 and y=100, you may choose a=3 and b=1, so that x becomes equal to 100⋅1⋅1⋅1=100;
if x=42 and y=13, there is no answer since you cannot decrease x with the given operations.
Input
The first line contains one integer t (1≤t≤104) — the number of test cases.

Each test case consists of one line containing two integers x and y (1≤x,y≤100).

Output
If it is possible to choose a pair of positive integers a and b so that x becomes y after the aforementioned process, print these two integers. The integers you print should be not less than 1 and not greater than 109 (it can be shown that if the answer exists, there is a pair of integers a and b meeting these constraints). If there are multiple such pairs, print any of them.

If it is impossible to choose a pair of integers a and b so that x becomes y, print the integer 0 twice.

Example
inputCopy
3
3 75
100 100
42 13
outputCopy
2 5
3 1
0 0
"""
