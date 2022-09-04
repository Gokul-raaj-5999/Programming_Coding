num = [9,8,7,6,5,4,3,2,1]

for _ in range(0, int(input())):
    n = int(input())
    s = ''
    i = 0
    while n > 0:
        if n >= num[i]:
            n-= num[i]
            s+= str(num[i])
        i+=1
        
    print(s[::-1])

"""
C. Minimum Varied Number
time limit per test1 second
memory limit per test256 megabytes
inputstandard input
outputstandard output
Find the minimum number with the given sum of digits s such that all digits in it are distinct (i.e. all digits are unique).

For example, if s=20, then the answer is 389. This is the minimum number in which all digits are different and the sum of the digits is 20 (3+8+9=20).

For the given s print the required number.

Input
The first line contains an integer t (1≤t≤45) — the number of test cases.

Each test case is specified by a line that contains the only integer s (1≤s≤45).

Output
Print t integers — the answers to the given test cases.

Example
inputCopy
4
20
8
45
10
outputCopy
389
8
123456789
19
"""
