def solve():
    n = int(input())
    type = 0
    if n%3 == 1:
        type = 1
    else:
        type = 2
    sum = 0
    while sum != n:
        print(type, end='')
        sum += type
        type = 3 - type
    print()



for _ in range(0, int(input())):
    ans = solve()
    # print(solve)

"""
A. Madoka and Math Dad
time limit per test1 second
memory limit per test256 megabytes
inputstandard input
outputstandard output
Madoka finally found the administrator password for her computer. Her father is a well-known popularizer of mathematics, so the password is the answer to the following problem.

Find the maximum decimal number without zeroes and with no equal digits in a row, such that the sum of its digits is n.

Madoka is too tired of math to solve it herself, so help her to solve this problem!

Input
Each test contains multiple test cases. The first line contains a single integer t (1≤t≤1000) — the number of test cases. Description of the test cases follows.

The only line of each test case contains an integer n (1≤n≤1000) — the required sum of the digits.

Output
For each test case print the maximum number you can obtain.

Example
inputCopy
5
1
2
3
4
5
outputCopy
1
2
21
121
212
Note
The only numbers with the sum of digits equal to 2 without zeros are 2 and 11. But the last one has two ones in a row, so it's not valid. That's why the answer is 2.

The only numbers with the sum of digits equal to 3 without zeros are 111, 12, 21, and 3. The first one has 2 ones in a row, so it's not valid. So the maximum valid number is 21.

The only numbers with the sum of digits equals to 4 without zeros are 1111, 211, 121, 112, 13, 31, 22, and 4. Numbers 1111, 211, 112, 22 aren't valid, because they have some identical digits in a row. So the maximum valid number is 121.

"""