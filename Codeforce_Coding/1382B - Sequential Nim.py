t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]
    for i in range(n):
        if a[i] != 1:
            break
    print('Second' if i&1 else 'First')



"""
B. Sequential Nim
time limit per test1 second
memory limit per test256 megabytes
inputstandard input
outputstandard output
There are n piles of stones, where the i-th pile has ai stones. Two people play a game, where they take alternating turns removing stones.

In a move, a player may remove a positive number of stones from the first non-empty pile (the pile with the minimal index, that has at least one stone). The first player who cannot make a move (because all piles are empty) loses the game. If both players play optimally, determine the winner of the game.

Input
The first line contains a single integer t (1≤t≤1000)  — the number of test cases. Next 2t lines contain descriptions of test cases.

The first line of each test case contains a single integer n (1≤n≤105)  — the number of piles.

The second line of each test case contains n integers a1,…,an (1≤ai≤109)  — ai is equal to the number of stones in the i-th pile.

It is guaranteed that the sum of n for all test cases does not exceed 105.

Output
For each test case, if the player who makes the first move will win, output "First". Otherwise, output "Second".

Example
inputCopy
7
3
2 5 4
8
1 1 1 1 1 1 1 1
6
1 2 3 4 5 6
6
1 1 2 1 2 2
1
1000000000
5
1 2 2 1 1
3
1 1 1
outputCopy
First
Second
Second
First
First
Second
First
Note
In the first test case, the first player will win the game. His winning strategy is:

The first player should take the stones from the first pile. He will take 1 stone. The numbers of stones in piles will be [1,5,4].
The second player should take the stones from the first pile. He will take 1 stone because he can't take any other number of stones. The numbers of stones in piles will be [0,5,4].
The first player should take the stones from the second pile because the first pile is empty. He will take 4 stones. The numbers of stones in piles will be [0,1,4].
The second player should take the stones from the second pile because the first pile is empty. He will take 1 stone because he can't take any other number of stones. The numbers of stones in piles will be [0,0,4].
The first player should take the stones from the third pile because the first and second piles are empty. He will take 4 stones. The numbers of stones in piles will be [0,0,0].
The second player will lose the game because all piles will be empty.
"""