n = int(input())
if(n%2==0):
    enum = n//2
    onum = n//2
    esum = enum*(enum+1)
    osum = onum**2
    print(esum-osum)
else:
    onum = (n-1)//2 + 1
    enum = (n-1)//2
    esum = enum*(enum+1)
    osum = onum**2
    print(esum-osum)

"""
For a positive integer n let's define a function f:

f(n) =  - 1 + 2 - 3 + .. + ( - 1)nn

Your task is to calculate f(n) for a given integer n.

Input
The single line contains the positive integer n (1 ≤ n ≤ 1015).

Output
Print f(n) in a single line.

Examples
inputCopy
4
outputCopy
2
inputCopy
5
outputCopy
-3
Note
f(4) =  - 1 + 2 - 3 + 4 = 2

f(5) =  - 1 + 2 - 3 + 4 - 5 =  - 3

"""
