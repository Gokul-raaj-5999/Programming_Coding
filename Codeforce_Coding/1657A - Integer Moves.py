for _ in range(0, int(input())):
    x, y = map(int, input().split())
    
    d = x**2 + y**2
    r = 0
    while (r**2 < d):
        r+=1
    ans = 2
    if r**2 == d:
        ans = 1
    if x == 0 and y == 0:
        ans = 0
    print(ans)
        

"""
A. Integer Moves
time limit per test2 seconds
memory limit per test256 megabytes
inputstandard input
outputstandard output
There's a chip in the point (0,0) of the coordinate plane. In one operation, you can move the chip from some point (x1,y1) to some point (x2,y2) if the Euclidean distance between these two points is an integer (i.e. (x1−x2)2+(y1−y2)2−−−−−−−−−−−−−−−−−−√ is integer).

Your task is to determine the minimum number of operations required to move the chip from the point (0,0) to the point (x,y).

Input
The first line contains a single integer t (1≤t≤3000) — number of test cases.

The single line of each test case contains two integers x and y (0≤x,y≤50) — the coordinates of the destination point.

Output
For each test case, print one integer — the minimum number of operations required to move the chip from the point (0,0) to the point (x,y).

Example
inputCopy
3
8 6
0 0
9 15
outputCopy
1
0
2
Note
In the first example, one operation (0,0)→(8,6) is enough. (0−8)2+(0−6)2−−−−−−−−−−−−−−−√=64+36−−−−−−√=100−−−√=10 is an integer.

In the second example, the chip is already at the destination point.

In the third example, the chip can be moved as follows: (0,0)→(5,12)→(9,15). (0−5)2+(0−12)2−−−−−−−−−−−−−−−−√=25+144−−−−−−−√=169−−−√=13 and (5−9)2+(12−15)2−−−−−−−−−−−−−−−−−√=16+9−−−−−√=25−−√=5 are integers.

"""
