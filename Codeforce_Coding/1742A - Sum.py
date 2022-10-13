def solve():
    a,b,c = list(map(int, input().split()))
    if a == b+c or b == a+c or c == a+b:
        return 'YES'
    else:
        return 'NO'
    
    
for t in range(0, int(input())):
    print(solve())

"""
A. Sum
time limit per test1 second
memory limit per test256 megabytes
inputstandard input
outputstandard output
You are given three integers a, b, and c. Determine if one of them is the sum of the other two.

Input
The first line contains a single integer t (1≤t≤9261) — the number of test cases.

The description of each test case consists of three integers a, b, c (0≤a,b,c≤20).

Output
For each test case, output "YES" if one of the numbers is the sum of the other two, and "NO" otherwise.

You can output the answer in any case (for example, the strings "yEs", "yes", "Yes" and "YES" will be recognized as a positive answer).

Example
inputCopy
7
1 4 3
2 5 8
9 11 20
0 0 0
20 20 20
4 12 3
15 7 8
outputCopy
YES
NO
YES
YES
NO
NO
YES
Note
In the first test case, 1+3=4.

In the second test case, none of the numbers is the sum of the other two.

In the third test case, 9+11=20.

"""