for _ in range(0, int(input())):
    n = int(input())
    s = input()
    mas = ''
    for ele in s:
        if ele == 'U':
            mas += 'D'
        elif ele == 'D':
            mas += 'U'
        else:
            mas += ele
    print(mas)


"""
A. Domino Disaster
time limit per test2 seconds
memory limit per test256 megabytes
inputstandard input
outputstandard output
Alice has a grid with 2 rows and n columns. She fully covers the grid using n dominoes of size 1×2 — Alice may place them vertically or horizontally, and each cell should be covered by exactly one domino.

Now, she decided to show one row of the grid to Bob. Help Bob and figure out what the other row of the grid looks like!

Input
The input consists of multiple test cases. The first line contains an integer t (1≤t≤5000) — the number of test cases. The description of the test cases follows.

The first line of each test case contains an integer n (1≤n≤100) — the width of the grid.

The second line of each test case contains a string s consisting of n characters, each of which is either L, R, U, or D, representing the left, right, top, or bottom half of a domino, respectively (see notes for better understanding). This string represents one of the rows of the grid.

Additional constraint on the input: each input corresponds to at least one valid tiling.

Output
For each test case, output one string — the other row of the grid, using the same format as the input string. If there are multiple answers, print any.

Example
inputCopy
4
1
U
2
LR
5
LRDLR
6
UUUUUU
outputCopy
D
LR
LRULR
DDDDDD
Note
In the first test case, Alice shows Bob the top row, the whole grid may look like:


In the second test case, Alice shows Bob the bottom row, the whole grid may look like:


In the third test case, Alice shows Bob the bottom row, the whole grid may look like:


In the fourth test case, Alice shows Bob the top row, the whole grid may look like:

"""
