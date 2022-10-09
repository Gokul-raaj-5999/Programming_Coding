n = int(input())
if n == 1:
    print(1)
    print(1)
else:

    a = []
    i = 1
    s = 1
    while s <= n:
        a.append(i)
        i += 1
        s += i

    # print(a)
    rem = n - sum(a)
    if rem <= a[-1]:
        a[-1] += rem
    else:
        a.append(rem)
    print(len(a))
    print(' '.join(str(x) for x in a))


"""
A. Santa Claus and Candies
time limit per test1 second
memory limit per test256 megabytes
inputstandard input
outputstandard output
Santa Claus has n candies, he dreams to give them as gifts to children.

What is the maximal number of children for whose he can give candies if Santa Claus want each kid should get distinct positive integer number of candies. Santa Class wants to give all n candies he has.

Input
The only line contains positive integer number n (1 ≤ n ≤ 1000) — number of candies Santa Claus has.

Output
Print to the first line integer number k — maximal number of kids which can get candies.

Print to the second line k distinct integer numbers: number of candies for each of k kid. The sum of k printed numbers should be exactly n.

If there are many solutions, print any of them.

Examples
inputCopy
5
outputCopy
2
2 3
inputCopy
9
outputCopy
3
3 5 1
inputCopy
2
outputCopy
1
2 """