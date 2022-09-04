n = int(input())
a = list(map(int, input().split()))

dic = {}

for i in range(0, n):
    if i == n-1:
        dic[i+1] = abs(a[i]- a[0])
        
    else:
        
        dic[i+1] = abs(a[i] - a[i+1])
        
m = 99999
ind = 0
for i in dic:
    if dic[i] < m:
        ind = i
        m = dic[i]
if ind == n:
    print(ind, 1)
else:
    print(ind, ind+1)
        
    

"""
A. Reconnaissance 2
time limit per test2 seconds
memory limit per test256 megabytes
inputstandard input
outputstandard output
n soldiers stand in a circle. For each soldier his height ai is known. A reconnaissance unit can be made of such two neighbouring soldiers, whose heights difference is minimal, i.e. |ai - aj| is minimal. So each of them will be less noticeable with the other. Output any pair of soldiers that can form a reconnaissance unit.

Input
The first line contains integer n (2 ≤ n ≤ 100) — amount of soldiers. Then follow the heights of the soldiers in their order in the circle — n space-separated integers a1, a2, ..., an (1 ≤ ai ≤ 1000). The soldier heights are given in clockwise or counterclockwise direction.

Output
Output two integers — indexes of neighbouring soldiers, who should form a reconnaissance unit. If there are many optimum solutions, output any of them. Remember, that the soldiers stand in a circle.

Examples
inputCopy
5
10 12 13 15 10
outputCopy
5 1
inputCopy
4
10 20 30 40
outputCopy
1 2
"""
