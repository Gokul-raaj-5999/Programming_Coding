n, m, a, b = list(map(int, input().split()))

p = n*a
c = ((n//m)+1)*b

combo = n//m
if(combo > 0):
    n = n%m
    pc = combo*b
    pc+= n*a
    print(min(p,c,pc))
else:
    print(min(p,c))
    

"""
A. Cheap Travel
time limit per test1 second
memory limit per test256 megabytes
inputstandard input
outputstandard output
Ann has recently started commuting by subway. We know that a one ride subway ticket costs a rubles. Besides, Ann found out that she can buy a special ticket for m rides (she can buy it several times). It costs b rubles. Ann did the math; she will need to use subway n times. Help Ann, tell her what is the minimum sum of money she will have to spend to make n rides?

Input
The single line contains four space-separated integers n, m, a, b (1 ≤ n, m, a, b ≤ 1000) — the number of rides Ann has planned, the number of rides covered by the m ride ticket, the price of a one ride ticket and the price of an m ride ticket.

Output
Print a single integer — the minimum sum in rubles that Ann will need to spend.

Examples
inputCopy
6 2 1 2
outputCopy
6
inputCopy
5 2 2 3
outputCopy
8
Note
In the first sample one of the optimal solutions is: each time buy a one ride ticket. There are other optimal solutions. For example, buy three m ride tickets.
"""
