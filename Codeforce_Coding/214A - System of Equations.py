n, m = map(int, input().split())
count = 0
if (n == 1 and m == 1):
    print(2)
else:
    for i in range(0, max(m,n)//2 +1):
        for j in range(0, max(m,n)//2 + 1):
            a,b = i, j
            if (n == a**2 +b) and (m == b**2 + a):
                count+= 1
            # print(n,a**2 +b, m,  b**2 + a )
    print(count)


"""
A. System of Equations
time limit per test2 seconds
memory limit per test256 megabytes
inputstandard input
outputstandard output
Furik loves math lessons very much, so he doesn't attend them, unlike Rubik. But now Furik wants to get a good mark for math. For that Ms. Ivanova, his math teacher, gave him a new task. Furik solved the task immediately. Can you?

You are given a system of equations:


You should count, how many there are pairs of integers (a, b) (0 ≤ a, b) which satisfy the system.

Input
A single line contains two integers n, m (1 ≤ n, m ≤ 1000) — the parameters of the system. The numbers on the line are separated by a space.

Output
On a single line print the answer to the problem.

Examples
inputCopy
9 3
outputCopy
1
inputCopy
14 28
outputCopy
1
inputCopy
4 20
outputCopy
0
Note
In the first sample the suitable pair is integers (3, 0). In the second sample the suitable pair is integers (3, 5). In the third sample there is no suitable pair.

"""
