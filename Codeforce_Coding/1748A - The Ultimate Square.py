import math 

def solve():
    n = int(input())
    print(math.ceil(n/2))

for t in range(0, int(input())):
    solve()




"""
A. The Ultimate Square
time limit per test1 second
memory limit per test256 megabytes
inputstandard input
outputstandard output
You have n rectangular wooden blocks, which are numbered from 1 to n. The i-th block is 1 unit high and ⌈i2⌉ units long.

Here, ⌈x2⌉ denotes the result of division of x by 2, rounded up. For example, ⌈42⌉=2 and ⌈52⌉=⌈2.5⌉=3.

For example, if n=5, then the blocks have the following sizes: 1×1, 1×1, 1×2, 1×2, 1×3.

The available blocks for n=5
Find the maximum possible side length of a square you can create using these blocks, without rotating any of them. Note that you don't have to use all of the blocks.

One of the ways to create 3×3 square using blocks 1 through 5
Input
Each test contains multiple test cases. The first line contains a single integer t (1≤t≤104) — the number of test cases.

The first line of each test case contains a single integer n (1≤n≤109) — the number of blocks.

Output
For each test case, print one integer — the maximum possible side length of a square you can create.

Example
inputCopy
3
2
5
197654321
outputCopy
1
3
98827161
Note
In the first test case, you can create a 1×1 square using only one of the blocks.

In the second test case, one of the possible ways to create a 3×3 square is shown in the statement. It is impossible to create a 4×4 or larger square, so the answer is 3.

"""