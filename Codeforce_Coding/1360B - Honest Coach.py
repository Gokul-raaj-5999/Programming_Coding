for _ in range(0,int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    # print('---------------st')
    # print(arr)
    sarr = arr
    # print(sarr)
    dic = {}
    split = -1
    for i in sarr:
        if(i in dic):
            dic[i] += 1
            split = i
            break
        else:
            dic[i] = 1
    if(split > 0):
        print(0)
        # ind = arr.index(split)
        # print(ind)
        # print(arr[:ind+1], arr[ind+1:])
    else:
        if(len(sarr)%2==0):
            difarr = []
            for i in range(0,len(sarr)-1):
                difarr.append(abs(sarr[i]-sarr[i+1]))
            print(min(difarr))
                
            # mid,nex = sarr[len(sarr)//2],sarr[(len(sarr)//2)+1]
            # print(mid,nex)
            
        else:
            difarr = []
            for i in range(0,len(sarr)-1):
                difarr.append(abs(sarr[i]-sarr[i+1]))
            print(min(difarr))
            # mid,nex = sarr[len(sarr)//2],sarr[(len(sarr)//2)+1]
            # print(mid,nex)
            
    # print('---------------en')

            

"""
B. Honest Coach
time limit per test2 seconds
memory limit per test256 megabytes
inputstandard input
outputstandard output
There are n athletes in front of you. Athletes are numbered from 1 to n from left to right. You know the strength of each athlete — the athlete number i has the strength si.

You want to split all athletes into two teams. Each team must have at least one athlete, and each athlete must be exactly in one team.

You want the strongest athlete from the first team to differ as little as possible from the weakest athlete from the second team. Formally, you want to split the athletes into two teams A and B so that the value |max(A)−min(B)| is as small as possible, where max(A) is the maximum strength of an athlete from team A, and min(B) is the minimum strength of an athlete from team B.

For example, if n=5 and the strength of the athletes is s=[3,1,2,6,4], then one of the possible split into teams is:

first team: A=[1,2,4],
second team: B=[3,6].
In this case, the value |max(A)−min(B)| will be equal to |4−3|=1. This example illustrates one of the ways of optimal split into two teams.

Print the minimum value |max(A)−min(B)|.

Input
The first line contains an integer t (1≤t≤1000) — the number of test cases in the input. Then t test cases follow.

Each test case consists of two lines.

The first line contains positive integer n (2≤n≤50) — number of athletes.

The second line contains n positive integers s1,s2,…,sn (1≤si≤1000), where si — is the strength of the i-th athlete. Please note that s values may not be distinct.

Output
For each test case print one integer — the minimum value of |max(A)−min(B)| with the optimal split of all athletes into two teams. Each of the athletes must be a member of exactly one of the two teams.

Example
inputCopy
5
5
3 1 2 6 4
6
2 1 3 2 4 3
4
7 9 3 1
2
1 1000
3
100 150 200
outputCopy
1
0
2
999
50
Note
The first test case was explained in the statement. In the second test case, one of the optimal splits is A=[2,1], B=[3,2,4,3], so the answer is |2−2|=0.

"""
