n = int(input())
ar = list(map(int, input().split()))

ar.sort()
dic = {}
for i in ar:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
        
m = 0
for i in dic:
    if dic[i] > m:
        m = dic[i]
        
print(m)

"""
A. Polycarp's Pockets
time limit per test1 second
memory limit per test256 megabytes
inputstandard input
outputstandard output
Polycarp has n coins, the value of the i-th coin is ai. Polycarp wants to distribute all the coins between his pockets, but he cannot put two coins with the same value into the same pocket.

For example, if Polycarp has got six coins represented as an array a=[1,2,4,3,3,2], he can distribute the coins into two pockets as follows: [1,2,3],[2,3,4].

Polycarp wants to distribute all the coins with the minimum number of used pockets. Help him to do that.

Input
The first line of the input contains one integer n (1≤n≤100) — the number of coins.

The second line of the input contains n integers a1,a2,…,an (1≤ai≤100) — values of coins.

Output
Print only one integer — the minimum number of pockets Polycarp needs to distribute all the coins so no two coins with the same value are put into the same pocket.

Examples
inputCopy
6
1 2 4 3 3 2
outputCopy
2
inputCopy
1
100
outputCopy
1
"""
