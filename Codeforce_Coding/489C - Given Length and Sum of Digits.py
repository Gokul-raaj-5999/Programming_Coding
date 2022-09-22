n, s = map(int, input().split())
if n==1 and s==0:
    print('0 0')
elif (9*n) < s or s == 0:
    print('-1 -1')
else:
    k = 10**(n-1)
    for i in range(s-1):
        k += 10**(i//9)
    k2 = 0
    for i in range(s):
        k2 += 10**(n-1-i//9)
    print(k, k2)


"""
C. Given Length and Sum of Digits...
time limit per test1 second
memory limit per test256 megabytes
inputstandard input
outputstandard output
You have a positive integer m and a non-negative integer s. Your task is to find the smallest and the largest of the numbers that have length m and sum of digits s. The required numbers should be non-negative integers written in the decimal base without leading zeroes.

Input
The single line of the input contains a pair of integers m, s (1 ≤ m ≤ 100, 0 ≤ s ≤ 900) — the length and the sum of the digits of the required numbers.

Output
In the output print the pair of the required non-negative integer numbers — first the minimum possible number, then — the maximum possible number. If no numbers satisfying conditions required exist, print the pair of numbers "-1 -1" (without the quotes).

Examples
inputCopy
2 15
outputCopy
69 96
inputCopy
3 0
outputCopy
-1 -1
"""