def solve():
    n, m, x, y = list(map(int, input().split()))
    arr = []
    for i in range(n):
        arr.extend(list(map(str, input().split('*'))))
    # print(arr)
    cost = 0
    for ele in arr:
        l = len(ele)
        if l > 0:
            if y <= x*2:
                if l %2 == 0:
                    cost += (l//2)*y
                elif l == 1:
                    cost += x
                else:
                    cost += x
                    l -= 1
                    cost += (l//2)*y
            else:
                cost += l*x
    return cost



for t in range(0, int(input())):
    print(solve())


"""
B. New Theatre Square
time limit per test2 seconds
memory limit per test256 megabytes
inputstandard input
outputstandard output
You might have remembered Theatre square from the problem 1A. Now it's finally getting repaved.

The square still has a rectangular shape of n×m meters. However, the picture is about to get more complicated now. Let ai,j be the j-th square in the i-th row of the pavement.

You are given the picture of the squares:

if ai,j= "*", then the j-th square in the i-th row should be black;
if ai,j= ".", then the j-th square in the i-th row should be white.
The black squares are paved already. You have to pave the white squares. There are two options for pavement tiles:

1×1 tiles — each tile costs x burles and covers exactly 1 square;
1×2 tiles — each tile costs y burles and covers exactly 2 adjacent squares of the same row. Note that you are not allowed to rotate these tiles or cut them into 1×1 tiles.
You should cover all the white squares, no two tiles should overlap and no black squares should be covered by tiles.

What is the smallest total price of the tiles needed to cover all the white squares?

Input
The first line contains a single integer t (1≤t≤500) — the number of testcases. Then the description of t testcases follow.

The first line of each testcase contains four integers n, m, x and y (1≤n≤100; 1≤m≤1000; 1≤x,y≤1000) — the size of the Theatre square, the price of the 1×1 tile and the price of the 1×2 tile.

Each of the next n lines contains m characters. The j-th character in the i-th line is ai,j. If ai,j= "*", then the j-th square in the i-th row should be black, and if ai,j= ".", then the j-th square in the i-th row should be white.

It's guaranteed that the sum of n×m over all testcases doesn't exceed 105.

Output
For each testcase print a single integer — the smallest total price of the tiles needed to cover all the white squares in burles.

Example
inputCopy
4
1 1 10 1
.
1 2 10 1
..
2 1 10 1
.
.
3 3 3 7
..*
*..
.*.
outputCopy
10
1
20
18
Note
In the first testcase you are required to use a single 1×1 tile, even though 1×2 tile is cheaper. So the total price is 10 burles.

In the second testcase you can either use two 1×1 tiles and spend 20 burles or use a single 1×2 tile and spend 1 burle. The second option is cheaper, thus the answer is 1.

The third testcase shows that you can't rotate 1×2 tiles. You still have to use two 1×1 tiles for the total price of 20.

In the fourth testcase the cheapest way is to use 1×1 tiles everywhere. The total cost is 6⋅3=18."""