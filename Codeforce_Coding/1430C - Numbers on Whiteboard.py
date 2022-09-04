import math

t = int(input())
for _ in range(0, t):
    n = int(input())
    
    a = []
    op = []
    for i in range(1, n+1):
        a.append(i)
    
    # print(a)
    for i in range(0, n-1):
        # a.sort()
        x = a[-1]
        y = a[-2]
        ans = math.ceil( (x+y)/2)
        a.pop()
        a.pop()
        a.append(ans)
        op.append([x,y])
 
    sys.stdout.write(str(a[0]) + "\n")
    for i in op:
        sys.stdout.write(" ".join(map(str,i)) + "\n")


"""
C. Numbers on Whiteboard
time limit per test2 seconds
memory limit per test256 megabytes
inputstandard input
outputstandard output
Numbers 1,2,3,…n (each integer from 1 to n once) are written on a board. In one operation you can erase any two numbers a and b from the board and write one integer a+b2 rounded up instead.

You should perform the given operation n−1 times and make the resulting number that will be left on the board as small as possible.

For example, if n=4, the following course of action is optimal:

choose a=4 and b=2, so the new number is 3, and the whiteboard contains [1,3,3];
choose a=3 and b=3, so the new number is 3, and the whiteboard contains [1,3];
choose a=1 and b=3, so the new number is 2, and the whiteboard contains [2].
It's easy to see that after n−1 operations, there will be left only one number. Your goal is to minimize it.

Input
The first line contains one integer t (1≤t≤1000) — the number of test cases.

The only line of each test case contains one integer n (2≤n≤2⋅105) — the number of integers written on the board initially.

It's guaranteed that the total sum of n over test cases doesn't exceed 2⋅105.

Output
For each test case, in the first line, print the minimum possible number left on the board after n−1 operations. Each of the next n−1 lines should contain two integers — numbers a and b chosen and erased in each operation.

Example
inputCopy
1
4
outputCopy
2
2 4
3 3
3 1
"""
