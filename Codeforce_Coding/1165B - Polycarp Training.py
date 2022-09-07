n = int(input())
a = list(map(int,input().split()))
pos = 1
a.sort()

for i in range(0, n):
    if a[i] >= pos:
        pos += 1

print(pos-1)

"""
B. Polycarp Training
time limit per test2 seconds
memory limit per test256 megabytes
inputstandard input
outputstandard output
Polycarp wants to train before another programming competition. During the first day of his training he should solve exactly 1 problem, during the second day — exactly 2 problems, during the third day — exactly 3 problems, and so on. During the k-th day he should solve k problems.

Polycarp has a list of n contests, the i-th contest consists of ai problems. During each day Polycarp has to choose exactly one of the contests he didn't solve yet and solve it. He solves exactly k problems from this contest. Other problems are discarded from it. If there are no contests consisting of at least k problems that Polycarp didn't solve yet during the k-th day, then Polycarp stops his training.

How many days Polycarp can train if he chooses the contests optimally?

Input
The first line of the input contains one integer n (1≤n≤2⋅105) — the number of contests.

The second line of the input contains n integers a1,a2,…,an (1≤ai≤2⋅105) — the number of problems in the i-th contest.

Output
Print one integer — the maximum number of days Polycarp can train if he chooses the contests optimally.

Examples
inputCopy
4
3 1 4 1
outputCopy
3
inputCopy
3
1 1 1
outputCopy
1
inputCopy
5
1 1 1 2 2
outputCopy
2
"""
