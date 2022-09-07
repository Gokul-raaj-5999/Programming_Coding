import math

def sumof(n):
    s = str(n)
    sum = 0
    for i in s:
        sum += int(i)
    return sum

for _ in range(0, int(input())):
    n = int(input())
    s = sumof(n)
    g = math.gcd(n, s)

    while g == 1:
        n += 1
        s = sumof(n)
        g = math.gcd(n, s)
    print(n)


"""
A. GCD Sum
time limit per test1 second
memory limit per test256 megabytes
inputstandard input
outputstandard output
The gcdSum of a positive integer is the gcd of that integer with its sum of digits. Formally, gcdSum(x)=gcd(x, sum of digits of x) for a positive integer x. gcd(a,b) denotes the greatest common divisor of a and b — the largest integer d such that both integers a and b are divisible by d.

For example: gcdSum(762)=gcd(762,7+6+2)=gcd(762,15)=3.

Given an integer n, find the smallest integer x≥n such that gcdSum(x)>1.

Input
The first line of input contains one integer t (1≤t≤104) — the number of test cases.

Then t lines follow, each containing a single integer n (1≤n≤1018).

All test cases in one test are different.

Output
Output t lines, where the i-th line is a single integer containing the answer to the i-th test case.

Example
inputCopy
3
11
31
75
outputCopy
12
33
75
Note
Let us explain the three test cases in the sample.

Test case 1: n=11:

gcdSum(11)=gcd(11,1+1)=gcd(11, 2)=1.

gcdSum(12)=gcd(12,1+2)=gcd(12, 3)=3.

So the smallest number ≥11 whose gcdSum >1 is 12.

Test case 2: n=31:

gcdSum(31)=gcd(31,3+1)=gcd(31, 4)=1.

gcdSum(32)=gcd(32,3+2)=gcd(32, 5)=1.

gcdSum(33)=gcd(33,3+3)=gcd(33, 6)=3.

So the smallest number ≥31 whose gcdSum >1 is 33.

Test case 3:  n=75:

gcdSum(75)=gcd(75,7+5)=gcd(75, 12)=3.

The gcdSum of 75 is already >1. Hence, it is the answer.

"""
        