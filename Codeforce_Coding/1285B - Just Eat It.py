t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    s=sum(l)
    k=0
    f=True
    for i in range(n-1):
        k=k+l[i]
        if k<=0 or k>=s:
            f=False
            print("NO")
            break
    if f:
        print("YES")

"""B. Just Eat It!
time limit per test1 second
memory limit per test256 megabytes
inputstandard input
outputstandard output
Today, Yasser and Adel are at the shop buying cupcakes. There are n cupcake types, arranged from 1 to n on the shelf, and there are infinitely many of each type. The tastiness of a cupcake of type i is an integer ai. There are both tasty and nasty cupcakes, so the tastiness can be positive, zero or negative.

Yasser, of course, wants to try them all, so he will buy exactly one cupcake of each type.

On the other hand, Adel will choose some segment [l,r] (1≤l≤r≤n) that does not include all of cupcakes (he can't choose [l,r]=[1,n]) and buy exactly one cupcake of each of types l,l+1,…,r.

After that they will compare the total tastiness of the cupcakes each of them have bought. Yasser will be happy if the total tastiness of cupcakes he buys is strictly greater than the total tastiness of cupcakes Adel buys regardless of Adel's choice.

For example, let the tastinesses of the cupcakes be [7,4,−1]. Yasser will buy all of them, the total tastiness will be 7+4−1=10. Adel can choose segments [7],[4],[−1],[7,4] or [4,−1], their total tastinesses are 7,4,−1,11 and 3, respectively. Adel can choose segment with tastiness 11, and as 10 is not strictly greater than 11, Yasser won't be happy :(

Find out if Yasser will be happy after visiting the shop.

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1≤t≤104). The description of the test cases follows.

The first line of each test case contains n (2≤n≤105).

The second line of each test case contains n integers a1,a2,…,an (−109≤ai≤109), where ai represents the tastiness of the i-th type of cupcake.

It is guaranteed that the sum of n over all test cases doesn't exceed 105.

Output
For each test case, print "YES", if the total tastiness of cupcakes Yasser buys will always be strictly greater than the total tastiness of cupcakes Adel buys regardless of Adel's choice. Otherwise, print "NO".

Example
inputCopy
3
4
1 2 3 4
3
7 4 -1
3
5 -5 5
outputCopy
YES
NO
NO
Note
In the first example, the total tastiness of any segment Adel can choose is less than the total tastiness of all cupcakes.

In the second example, Adel will choose the segment [1,2] with total tastiness 11, which is not less than the total tastiness of all cupcakes, which is 10.

In the third example, Adel can choose the segment [3,3] with total tastiness of 5. Note that Yasser's cupcakes' total tastiness is also 5, so in that case, the total tastiness of Yasser's cupcakes isn't strictly greater than the total tastiness of Adel's cupcakes.

"""