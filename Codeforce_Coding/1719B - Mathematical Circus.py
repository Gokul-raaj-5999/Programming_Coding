t = int(input())
for _ in range(0, t):
    n, k = map(int, input().split())

    k = k%4
    if k == 0:
        print('NO')
    elif k ==1 or k ==3:
        print('YES')
        for i in range(1, n+1, 2):
            print(i, i+1)
    else:
        print('YES')
        for i in range(3, n+1, 4):
            print(i, i+1)
        for i in range(1, n+1, 4):
            print(i+1, i)



"""
B. Mathematical Circus
time limit per test1 second
memory limit per test256 megabytes
inputstandard input
outputstandard output
A new entertainment has appeared in Buryatia — a mathematical circus! The magician shows two numbers to the audience — n and k, where n is even. Next, he takes all the integers from 1 to n, and splits them all into pairs (a,b) (each integer must be in exactly one pair) so that for each pair the integer (a+k)⋅b is divisible by 4 (note that the order of the numbers in the pair matters), or reports that, unfortunately for viewers, such a split is impossible.

Burenka really likes such performances, so she asked her friend Tonya to be a magician, and also gave him the numbers n and k.

Tonya is a wolf, and as you know, wolves do not perform in the circus, even in a mathematical one. Therefore, he asks you to help him. Let him know if a suitable splitting into pairs is possible, and if possible, then tell it.

Input
The first line contains one integer t (1≤t≤104) — the number of test cases. The following is a description of the input data sets.

The single line of each test case contains two integers n and k (2≤n≤2⋅105, 0≤k≤109, n is even) — the number of integers and the number being added k.

It is guaranteed that the sum of n over all test cases does not exceed 2⋅105.

Output
For each test case, first output the string "YES" if there is a split into pairs, and "NO" if there is none.

If there is a split, then in the following n2 lines output pairs of the split, in each line print 2 numbers — first the integer a, then the integer b.

Example
inputCopy
4
4 1
2 0
12 10
14 11
outputCopy
YES
1 2
3 4
NO
YES
3 4
7 8
11 12
2 1
6 5
10 9
YES
1 2
3 4
5 6
7 8
9 10
11 12
13 14
Note
In the first test case, splitting into pairs (1,2) and (3,4) is suitable, same as splitting into (1,4) and (3,2).

In the second test case, (1+0)⋅2=1⋅(2+0)=2 is not divisible by 4, so there is no partition.

"""
