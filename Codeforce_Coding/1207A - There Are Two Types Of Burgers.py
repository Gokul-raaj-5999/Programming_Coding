for t in range(0, int(input())):
    b, p, f = list(map(int, input().split()))
    h ,c = map(int, input().split())
    res = 0

    b //= 2
    if(h < c):
        h, c = c, h
        p, f = f, p


    cnt = min(b, p)
    b -= cnt
    p -= cnt
    res += h * cnt; 
    
    cnt = min(b, f)
    b -= cnt
    f -= cnt
    res += c * cnt       

    print(res)
    # print()


"""
A. There Are Two Types Of Burgers
time limit per test1 second
memory limit per test256 megabytes
inputstandard input
outputstandard output
There are two types of burgers in your restaurant — hamburgers and chicken burgers! To assemble a hamburger you need two buns and a beef patty. To assemble a chicken burger you need two buns and a chicken cutlet.

You have b buns, p beef patties and f chicken cutlets in your restaurant. You can sell one hamburger for h dollars and one chicken burger for c dollars. Calculate the maximum profit you can achieve.

You have to answer t independent queries.

Input
The first line contains one integer t (1≤t≤100) – the number of queries.

The first line of each query contains three integers b, p and f (1≤b, p, f≤100) — the number of buns, beef patties and chicken cutlets in your restaurant.

The second line of each query contains two integers h and c (1≤h, c≤100) — the hamburger and chicken burger prices in your restaurant.

Output
For each query print one integer — the maximum profit you can achieve.

Example
inputCopy
3
15 2 3
5 10
7 5 2
10 12
1 100 100
100 100
outputCopy
40
34
0
Note
In first query you have to sell two hamburgers and three chicken burgers. Your income is 2⋅5+3⋅10=40.

In second query you have to ell one hamburgers and two chicken burgers. Your income is 1⋅10+2⋅12=34.

In third query you can not create any type of burgers because because you have only one bun. So your income is zero.





"""