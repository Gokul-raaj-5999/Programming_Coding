def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    zarr = []
    oarr = []

    for i in range(0, n):
        if a[i] == 0:
            zarr.append(b[i])
        else:
            oarr.append(b[i])

    if len(zarr) > 0 and len(oarr) > 0:
        zarr.sort()
        oarr.sort()
        zl, ol = len(zarr), len(oarr)
        if zl == ol:
            if zarr[0] <= oarr[0]:
                ini = zarr[0]
                zarr = zarr[1:]
                zarr.sort(reverse= True)
                oarr.sort(reverse= True)
            else:
                ini = oarr[0]
                oarr = oarr[1:]
                zarr.sort(reverse= True)
                oarr.sort(reverse= True)
            zl, ol = len(zarr), len(oarr)
            tot = ini
            if zl <= ol:
                for i in range(0, zl):
                    tot += 2*(zarr[i])
                    tot += 2*(oarr[i])
                tot += 2*oarr[zl]
                tot += sum(oarr[zl+1:])

            else:
                for i in range(0, ol):
                    tot += 2*(zarr[i])
                    tot += 2*(oarr[i])
                tot += 2*zarr[ol]
                tot += sum(zarr[ol+1:])
 
        elif zl< ol:
            ini = oarr[0]
            oarr = oarr[1:]
            zarr.sort(reverse= True)
            oarr.sort(reverse= True)
            zl, ol = len(zarr), len(oarr)
            tot = ini
            if zl <= ol:
                for i in range(0, zl):
                    tot += 2*(zarr[i])
                    tot += 2*(oarr[i])
                tot += sum(oarr[zl:])

            else:
                for i in range(0, ol):
                    tot += 2*(zarr[i])
                    tot += 2*(oarr[i])
                tot += sum(zarr[ol:])

        else:
            ini = zarr[0]
            zarr = zarr[1:]
            zarr.sort(reverse= True)
            oarr.sort(reverse= True)
            zl, ol = len(zarr), len(oarr)
            tot = ini
            if zl <= ol:
                for i in range(0, zl):
                    tot += 2*(zarr[i])
                    tot += 2*(oarr[i])
                tot += sum(oarr[zl:])

            else:
                for i in range(0, ol):
                    tot += 2*(zarr[i])
                    tot += 2*(oarr[i])
                tot += sum(zarr[ol:])

    else:
        tot = 0
        tot += sum(zarr)
        tot += sum(oarr)
    
    return tot


for t in range(0, int(input())):
    print(solve())
    # print()



"""
A. Glory Addicts
time limit per test2 seconds
memory limit per test512 megabytes
inputstandard input
outputstandard output
The hero is addicted to glory, and is fighting against a monster.

The hero has n skills. The i-th skill is of type ai (either fire or frost) and has initial damage bi.

The hero can perform all of the n skills in any order (with each skill performed exactly once). When performing each skill, the hero can play a magic as follows:

If the current skill immediately follows another skill of a different type, then its damage is doubled.
In other words,
If a skill of type fire and with initial damage c is performed immediately after a skill of type fire, then it will deal c damage;
If a skill of type fire and with initial damage c is performed immediately after a skill of type frost, then it will deal 2c damage;
If a skill of type frost and with initial damage c is performed immediately after a skill of type fire, then it will deal 2c damage;
If a skill of type frost and with initial damage c is performed immediately after a skill of type frost , then it will deal c damage.
Your task is to find the maximum damage the hero can deal.

Input
Each test contains multiple test cases. The first line contains an integer t (1≤t≤105) — the number of test cases. The following lines contain the description of each test case.

The first line of each test case contains an integer n (1≤n≤105), indicating the number of skills.

The second line of each test case contains n integers a1,a2,…,an (0≤ai≤1), where ai indicates the type of the i-th skill. Specifically, the i-th skill is of type fire if ai=0, and of type frost if ai=1.

The third line of each test case contains n integers b1,b2,…,bn (1≤bi≤109), where bi indicates the initial damage of the i-th skill.

It is guaranteed that the sum of n over all test cases does not exceed 105.

Output
For each test case, output the maximum damage the hero can deal.

Example
inputCopy
4
4
0 1 1 1
1 10 100 1000
6
0 0 0 1 1 1
3 4 5 6 7 8
3
1 1 1
1000000000 1000000000 1000000000
1
1
1
outputCopy
2112
63
3000000000
1
Note
In the first test case, we can order the skills by [3,1,4,2], and the total damage is 100+2×1+2×1000+10=2112.

In the second test case, we can order the skills by [1,4,2,5,3,6], and the total damage is 3+2×6+2×4+2×7+2×5+2×8=63.

In the third test case, we can order the skills by [1,2,3], and the total damage is 1000000000+1000000000+1000000000=3000000000.

In the fourth test case, there is only one skill with initial damage 1, so the total damage is 1.

"""