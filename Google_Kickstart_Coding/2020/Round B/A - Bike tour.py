def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    count = 0
    for i in range(1, n-1):
        if a[i] > a[i+1] and a[i-1] < a[i]:
            count += 1
    return(count)



for _ in range(0, int(input())):
    ans = solve()
    print(f'Case #{_+1}: {ans}')

"""

Bike Tour (5pts, 7pts)

Practice Submissions
Attempt 2
S
check
check
Sep 2 2022, 14:52
remove_red_eye
Attempt 1
S
WA
remove_circle_outline
Sep 2 2022, 14:51
remove_red_eye
Last updated: Sep 2 2022, 13:10

PROBLEM
ANALYSIS
Problem
Li has planned a bike tour through the mountains of Switzerland. His tour consists of N checkpoints, numbered from 1 to N in the order he will visit them. The i-th checkpoint has a height of Hi.

A checkpoint is a peak if:

It is not the 1st checkpoint or the N-th checkpoint, and
The height of the checkpoint is strictly greater than the checkpoint immediately before it and the checkpoint immediately after it.
Please help Li find out the number of peaks.

Input
The first line of the input gives the number of test cases, T. T test cases follow. Each test case begins with a line containing the integer N. The second line contains N integers. The i-th integer is Hi.

Output
For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the number of peaks in Li's bike tour.

Limits
Time limit: 10 seconds.
Memory limit: 1 GB.
1 ≤ T ≤ 100.
1 ≤ Hi ≤ 100.
Test Set 1
3 ≤ N ≤ 5.
Test Set 2
3 ≤ N ≤ 100.
Sample
Sample Input
save_alt
content_copy
4
3
10 20 14
4
7 7 7 7
5
10 90 20 90 10
3
10 3 10
Sample Output
save_alt
content_copy
Case #1: 1
Case #2: 0
Case #3: 2
Case #4: 0
In sample case #1, the 2nd checkpoint is a peak.
In sample case #2, there are no peaks.
In sample case #3, the 2nd and 4th checkpoint are peaks.
In sample case #4, there are no peaks.
"""
