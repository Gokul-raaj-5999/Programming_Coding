for _ in range(0, int(input())):
    l,r = map(int, input().split())
    
    num = r//2+1
    if num >= l :
        ans = (r%num)
    else:
        num = l
        ans = (r%num)
        
    print(ans)

"""
A. The Miracle and the Sleeper
time limit per test1 second
memory limit per test256 megabytes
inputstandard input
outputstandard output
You are given two integers l and r, l≤r. Find the largest possible value of amodb over all pairs (a,b) of integers for which r≥a≥b≥l.

As a reminder, amodb is a remainder we get when dividing a by b. For example, 26mod8=2.

Input
Each test contains multiple test cases.

The first line contains one positive integer t (1≤t≤104), denoting the number of test cases. Description of the test cases follows.

The only line of each test case contains two integers l, r (1≤l≤r≤109).

Output
For every test case, output the largest possible value of amodb over all pairs (a,b) of integers for which r≥a≥b≥l.

Example
inputCopy
4
1 1
999999999 1000000000
8 26
1 999999999
outputCopy
0
1
12
499999999
Note
In the first test case, the only allowed pair is (a,b)=(1,1), for which amodb=1mod1=0.

In the second test case, the optimal choice is pair (a,b)=(1000000000,999999999), for which amodb=1.

"""
