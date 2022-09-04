n = int(input())
ar = list(map(int, input().split()))
count = 1
vec = []
if(n > 1):
    for i in range(0, n-1):
        if (ar[i] < ar[i+1]):
            count+=1
        else:
            count = 1
        vec.append(count)
    print(max(vec))
else:
    print(1)

"""
A. Maximum Increase
time limit per test1 second
memory limit per test256 megabytes
inputstandard input
outputstandard output
You are given array consisting of n integers. Your task is to find the maximum length of an increasing subarray of the given array.

A subarray is the sequence of consecutive elements of the array. Subarray is called increasing if each element of this subarray strictly greater than previous.

Input
The first line contains single positive integer n (1 ≤ n ≤ 105) — the number of integers.

The second line contains n positive integers a1, a2, ..., an (1 ≤ ai ≤ 109).

Output
Print the maximum length of an increasing subarray of the given array.

Examples
inputCopy
5
1 7 2 11 15
outputCopy
3
inputCopy
6
100 100 100 100 100 100
outputCopy
1
inputCopy
3
1 2 3
outputCopy
3
"""
