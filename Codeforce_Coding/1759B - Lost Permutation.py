def solve():
    n, s = map(int, input().split())
    a = list(map(int, input().split()))

    r = sum(a)
    m = max(a)
    x = s + r
    t = 0
    i = 1
    while t < x:
        t += i
        i += 1
    if t == x and m <= i-1:
        return 'YES'
    else:
        return 'NO'
    



for t in range(0, int(input())):
    print(solve())



"""
B. Lost Permutation
time limit per test1 second
memory limit per test256 megabytes
inputstandard input
outputstandard output
A sequence of n numbers is called a permutation if it contains all integers from 1 to n exactly once. For example, the sequences [3,1,4,2], [1] and [2,1] are permutations, but [1,2,1], [0,1] and [1,3,4] — are not.

Polycarp lost his favorite permutation and found only some of its elements — the numbers b1,b2,…bm. He is sure that the sum of the lost elements equals s.

Determine whether one or more numbers can be appended to the given sequence b1,b2,…bm such that the sum of the added numbers equals s, and the resulting new array is a permutation?

Input
The first line of input contains a single integer t (1≤t≤100) —the number of test cases.

Then the descriptions of the test cases follow.

The first line of each test set contains two integers m and s (1≤m≤50, 1≤s≤1000)—-the number of found elements and the sum of forgotten numbers.

The second line of each test set contains m different integers b1,b2…bm (1≤bi≤50) — the elements Polycarp managed to find.

Output
Print t lines, each of which is the answer to the corresponding test set. Print as the answer YES if you can append several elements to the array b, that their sum equals s and the result will be a permutation. Output NO otherwise.

You can output the answer in any case (for example, yEs, yes, Yes and YES will be recognized as positive answer).

Example
inputCopy
5
3 13
3 1 4
1 1
1
3 3
1 4 2
2 1
4 3
5 6
1 2 3 4 5
outputCopy
YES
NO
YES
NO
YES
Note
In the test case of the example, m=3,s=13,b=[3,1,4]. You can append to b the numbers 6,2,5, the sum of which is 6+2+5=13. Note that the final array will become [3,1,4,6,2,5], which is a permutation.

In the second test case of the example, m=1,s=1,b=[1]. You cannot append one or more numbers to [1] such that their sum equals 1 and the result is a permutation.

In the third test case of the example, m=3,s=3,b=[1,4,2]. You can append the number 3 to b. Note that the resulting array will be [1,4,2,3], which is a permutation.

"""