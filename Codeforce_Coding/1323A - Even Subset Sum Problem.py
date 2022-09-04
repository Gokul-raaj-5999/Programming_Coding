for _ in range(0, int(input())):
    n = int(input())
    ar = list(map(int, input().split()))
    count = 0
    op = []
    for i in range(0, n):
        if ar[i]%2 == 0:
            print(1)
            print(i+1)
            break
        else:
            if count == 0:
                count+=1
                op.append(i+1)
            elif count == 1:
                count+=1
                op.append(i+1)
                print(count)
                print(' '.join(str(x) for x in op))
                break
    else:
        print(-1)

"""
A. Even Subset Sum Problem
time limit per test1 second
memory limit per test512 megabytes
inputstandard input
outputstandard output
You are given an array a consisting of n positive integers. Find a non-empty subset of its elements such that their sum is even (i.e. divisible by 2) or determine that there is no such subset.

Both the given array and required subset may contain equal values.

Input
The first line contains a single integer t (1≤t≤100), number of test cases to solve. Descriptions of t test cases follow.

A description of each test case consists of two lines. The first line contains a single integer n (1≤n≤100), length of array a.

The second line contains n integers a1,a2,…,an (1≤ai≤100), elements of a. The given array a can contain equal values (duplicates).

Output
For each test case output −1 if there is no such subset of elements. Otherwise output positive integer k, number of elements in the required subset. Then output k distinct integers (1≤pi≤n), indexes of the chosen elements. If there are multiple solutions output any of them.

Example
inputCopy
3
3
1 4 3
1
15
2
3 5
outputCopy
1
2
-1
2
1 2
Note
There are three test cases in the example.

In the first test case, you can choose the subset consisting of only the second element. Its sum is 4 and it is even.

In the second test case, there is only one non-empty subset of elements consisting of the first element, however sum in it is odd, so there is no solution.

In the third test case, the subset consisting of all array's elements has even sum.

"""
