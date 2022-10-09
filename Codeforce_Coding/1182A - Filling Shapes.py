n = int(input())
if n %2 == 0:
    ans = 2 ** (n//2)
else:
    ans = 0
print(ans)



"""
A. Filling Shapes
time limit per test1 second
memory limit per test256 megabytes
inputstandard input
outputstandard output
You have a given integer n. Find the number of ways to fill all 3×n tiles with the shape described in the picture below. Upon filling, no empty spaces are allowed. Shapes cannot overlap.

This picture describes when n=4. The left one is the shape and the right one is 3×n tiles.
Input
The only line contains one integer n (1≤n≤60) — the length.

Output
Print the number of ways to fill.

Examples
inputCopy
4
outputCopy
4
inputCopy
1
outputCopy
0
Note
In the first example, there are 4 possible cases of filling.

In the second example, you cannot fill the shapes in 3×1 tiles.

"""