def solve():
    n = int(input())
    a = list(map(int, input().split()))
    lst = []
    for ele in a:
        if ele in lst:
            lst.append(-ele)
        else:
            lst.append(ele)
    return(len(set(lst)))


for t in range(0, int(input())):
    ans = solve()
    print(ans)


"""
A. Integer Diversity
time limit per test1 second
memory limit per test256 megabytes
inputstandard input
outputstandard output
You are given n integers a1,a2,…,an. You choose any subset of the given numbers (possibly, none or all numbers) and negate these numbers (i. e. change x→(−x)). What is the maximum number of different values in the array you can achieve?

Input
The first line of input contains one integer t (1≤t≤100): the number of test cases.

The next lines contain the description of the t test cases, two lines per a test case.

In the first line you are given one integer n (1≤n≤100): the number of integers in the array.

The second line contains n integers a1,a2,…,an (−100≤ai≤100).

Output
For each test case, print one integer: the maximum number of different elements in the array that you can achieve negating numbers in the array.

Example
inputCopy
3
4
1 1 2 2
3
1 2 3
2
0 0
outputCopy
4
3
1
Note
In the first example we can, for example, negate the first and the last numbers, achieving the array [−1,1,2,−2] with four different values.

In the second example all three numbers are already different.

In the third example negation does not change anything.

"""