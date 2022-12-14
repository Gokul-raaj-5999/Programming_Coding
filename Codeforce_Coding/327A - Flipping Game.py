n = int(input())
A = [int(x) for x in input().split(' ')]
B = [0 for y in range(n)]
t = sum(A)
B[0] = 1 + t - 2*A[0]
i = 1

while(i < n):
    B[i] = max(B[i-1]+1-2*A[i],t + 1 - 2*A[i])
    i += 1

print(max(B))


"""
A. Flipping Game
time limit per test1 second
memory limit per test256 megabytes
inputstandard input
outputstandard output
Iahub got bored, so he invented a game to be played on paper.

He writes n integers a1, a2, ..., an. Each of those integers can be either 0 or 1. He's allowed to do exactly one move: he chooses two indices i and j (1 ≤ i ≤ j ≤ n) and flips all values ak for which their positions are in range [i, j] (that is i ≤ k ≤ j). Flip the value of x means to apply operation x = 1 - x.

The goal of the game is that after exactly one move to obtain the maximum number of ones. Write a program to solve the little game of Iahub.

Input
The first line of the input contains an integer n (1 ≤ n ≤ 100). In the second line of the input there are n integers: a1, a2, ..., an. It is guaranteed that each of those n values is either 0 or 1.

Output
Print an integer — the maximal number of 1s that can be obtained after exactly one move.

Examples
inputCopy
5
1 0 0 1 0
outputCopy
4
inputCopy
4
1 0 0 1
outputCopy
4
Note
In the first case, flip the segment from 2 to 5 (i = 2, j = 5). That flip changes the sequence, it becomes: [1 1 1 0 1]. So, it contains four ones. There is no way to make the whole sequence equal to [1 1 1 1 1].

In the second case, flipping only the second and the third element (i = 2, j = 3) will turn all numbers into 1.

"""