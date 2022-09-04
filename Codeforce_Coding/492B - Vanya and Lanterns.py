nlig, stdic = map(int, input().split())
arr = list(map(int, input().split()))
new = []

if(nlig > 1):
    arr.sort()
    # print(arr)
    for i in range(0,len(arr)-1):
        new.append(arr[i+1]-arr[i])
    
    # print(new)
    reqd = max(new)/2
    if(0 not in arr):
        dis = arr[0]
        if(dis > reqd):
            reqd = dis
    if(stdic not in arr):
        dis = stdic-arr[-1]
        if(dis > reqd):
            reqd = dis
        
    print('{0:.10f}'.format(reqd))
else:
    d1 = arr[0] - 0
    d2 = stdic - arr[0]
    print('{0:.10f}'.format(max(d1, d2)))


"""
B. Vanya and Lanterns
time limit per test1 second
memory limit per test256 megabytes
inputstandard input
outputstandard output
Vanya walks late at night along a straight street of length l, lit by n lanterns. Consider the coordinate system with the beginning of the street corresponding to the point 0, and its end corresponding to the point l. Then the i-th lantern is at the point ai. The lantern lights all points of the street that are at the distance of at most d from it, where d is some positive number, common for all lanterns.

Vanya wonders: what is the minimum light radius d should the lanterns have to light the whole street?

Input
The first line contains two integers n, l (1 ≤ n ≤ 1000, 1 ≤ l ≤ 109) — the number of lanterns and the length of the street respectively.

The next line contains n integers ai (0 ≤ ai ≤ l). Multiple lanterns can be located at the same point. The lanterns may be located at the ends of the street.

Output
Print the minimum light radius d, needed to light the whole street. The answer will be considered correct if its absolute or relative error doesn't exceed 10 - 9.

Examples
inputCopy
7 15
15 5 3 7 9 14 0
outputCopy
2.5000000000
inputCopy
2 5
2 5
outputCopy
2.0000000000
Note
Consider the second sample. At d = 2 the first lantern will light the segment [0, 4] of the street, and the second lantern will light segment [3, 5]. Thus, the whole street will be lit.

"""
