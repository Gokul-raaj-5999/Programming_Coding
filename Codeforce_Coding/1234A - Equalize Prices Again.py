import math

for _ in range(0 ,int(input())):
    n = int(input())
    ar = list(map(int, input().split()))
    s = sum(ar)
    print(math.ceil(s/n))

"""
A. Equalize Prices Again
time limit per test1 second
memory limit per test256 megabytes
inputstandard input
outputstandard output
You are both a shop keeper and a shop assistant at a small nearby shop. You have n goods, the i-th good costs ai coins.

You got tired of remembering the price of each product when customers ask for it, thus you decided to simplify your life. More precisely you decided to set the same price for all n goods you have.

However, you don't want to lose any money so you want to choose the price in such a way that the sum of new prices is not less than the sum of the initial prices. It means that if you sell all n goods for the new price, you will receive at least the same (or greater) amount of money as if you sell them for their initial prices.

On the other hand, you don't want to lose customers because of big prices so among all prices you can choose you need to choose the minimum one.

So you need to find the minimum possible equal price of all n goods so if you sell them for this price, you will receive at least the same (or greater) amount of money as if you sell them for their initial prices.

You have to answer q independent queries.

Input
The first line of the input contains one integer q (1≤q≤100) — the number of queries. Then q queries follow.

The first line of the query contains one integer n (1≤n≤100) — the number of goods. The second line of the query contains n integers a1,a2,…,an (1≤ai≤107), where ai is the price of the i-th good.

Output
For each query, print the answer for it — the minimum possible equal price of all n goods so if you sell them for this price, you will receive at least the same (or greater) amount of money as if you sell them for their initial prices.

Example
inputCopy
3
5
1 2 3 4 5
3
1 2 2
4
1 1 1 1
outputCopy
3
2
1
"""
