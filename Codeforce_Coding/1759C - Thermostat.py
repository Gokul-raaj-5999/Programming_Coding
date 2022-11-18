def solve():
    l, r, x = list(map(int, input().split()))
    a, b = map(int, input().split())

    if a == b:
        return 0
    if abs(a-b) >= x:
        return 1
    a, b = sorted([a,b])
    if a-x >= l or b+x <= r:
        return 2
    if a+x <= r and b-x >= l:
        return 3
    return -1


for t in range(0, int(input())):
    print(solve())




"""
C. Thermostat
time limit per test1 second
memory limit per test256 megabytes
inputstandard input
outputstandard output
Vlad came home and found out that someone had reconfigured the old thermostat to the temperature of a.

The thermostat can only be set to a temperature from l to r inclusive, the temperature cannot change by less than x. Formally, in one operation you can reconfigure the thermostat from temperature a to temperature b if |a−b|≥x and l≤b≤r.

You are given l, r, x, a and b. Find the minimum number of operations required to get temperature b from temperature a, or say that it is impossible.

Input
The first line of input data contains the single integer t (1≤t≤104) — the number of test cases in the test.

The descriptions of the test cases follow.

The first line of each case contains three integers l, r and x (−109≤l≤r≤109, 1≤x≤109) — range of temperature and minimum temperature change.

The second line of each case contains two integers a and b (l≤a,b≤r) — the initial and final temperatures.

Output
Output t numbers, each of which is the answer to the corresponding test case. If it is impossible to achieve the temperature b, output -1, otherwise output the minimum number of operations.

Example
inputCopy
10
3 5 6
3 3
0 15 5
4 5
0 10 5
3 7
3 5 6
3 4
-10 10 11
-5 6
-3 3 4
1 0
-5 10 8
9 2
1 5 1
2 5
-1 4 3
0 2
-6 3 6
-1 -4
outputCopy
0
2
3
-1
1
-1
3
1
3
-1
Note
In the first example, the thermostat is already set up correctly.

In the second example, you can achieve the desired temperature as follows: 4→10→5.

In the third example, you can achieve the desired temperature as follows: 3→8→2→7.

In the fourth test, it is impossible to make any operation.

"""