from collections import defaultdict

T = int(input())
for x in range(1, T + 1):
    N, Q = map(int, input().split())
    characters = input()
    counters = [defaultdict(int)]
    for character in characters:
        counter = counters[-1].copy()
        counter[character] += 1
        counters.append(counter)
    y = 0
    for i in range(Q):
        L, R = map(int, input().split())
        odd_encountered = False
        for letter, R_count in counters[R].items():
            if (R_count - counters[L - 1][letter]) % 2:
                if odd_encountered:
                    break
                odd_encountered = True
        else:
            y += 1
    print(f"Case #{x}: {y}", flush = True)


"""

Building Palindromes (6pts, 8pts)

Attempts

9

Penalties

8

Penalty Time

18:42:47

Points

done
Points

done
Practice Submissions
You have not attempted this problem.
Submissions
Attempt 9
S
check
check
18:42:47
remove_red_eye
Attempt 8
S
check
TLE
18:04:54
remove_red_eye
Attempt 7
S
check
MLE
17:57:31
remove_red_eye
Attempt 6
S
check
TLE
17:43:04
remove_red_eye
Attempt 5
S
check
TLE
17:35:30
remove_red_eye
Attempt 4
S
check
TLE
17:23:44
remove_red_eye
Attempt 3
S
check
TLE
17:17:33
remove_red_eye
Attempt 2
S
check
TLE
17:11:35
remove_red_eye
Attempt 1
S
WA
remove_circle_outline
17:08:41
remove_red_eye
Last updated: Sep 3 2022, 22:33

PROBLEM
ANALYSIS
Problem
Download the Starter Code!
Anna has a row of N blocks, each with exactly one letter from A to Z written on it. The blocks are numbered 1,2,⋯,N from left to right.

Today, she is learning about palindromes. A palindrome is a string that is the same written forwards and backwards. For example, ANNA, RACECAR, AAA and X are all palindromes, while AB, FROG and YOYO are not.

Bob wants to test how well Anna understands palindromes, and will ask her Q questions. The i-th question is: can Anna form a palindrome using all of the blocks numbered from Li to Ri, inclusive? She may rearrange the blocks if necessary. After each question, Anna puts the blocks back in their original positions.

Please help Anna by finding out how many of Bob's questions she can answer "yes" to.

Input
The first line of the input gives the number of test cases, T. T test cases follow. Each test case starts with a line containing the two integers N and Q, the number of blocks and the number of questions, respectively. Then, another line follows, containing a string of N uppercase characters (A to Z). Then, Q lines follow. The i-th line contains the two integers Li and Ri, describing the i-th question.

Output
For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the number of questions Anna can answer "yes" to.

Limits
Time limit: 30 seconds.
Memory limit: 1 GB.
1≤T≤100.
1≤Li≤Ri≤N.
Test Set 1
1≤N≤20.
1≤Q≤20.
Test Set 2
1≤N≤100000.
1≤Q≤100000.
Sample
Sample Input
save_alt
content_copy
2
7 5
ABAACCA
3 6
4 4
2 5
6 7
3 7
3 5
XYZ
1 3
1 3
1 3
1 3
1 3
Sample Output
save_alt
content_copy
Case #1: 3
Case #2: 0

In Sample Case #1, N = 7 and Q = 5.

For the first question, Anna must use the blocks AACC. She can rearrange these blocks into the palindrome ACCA (or CAAC).
For the second question, Anna must use the blocks A. This is already a palindrome, so she does not need to rearrange them.
For the third question, Anna must use the blocks BAAC. These blocks cannot be rearranged into a palindrome.
For the fourth question, Anna must use the blocks CA. These blocks cannot be rearranged into a palindrome.
For the fifth question, Anna must use the blocks AACCA. She can rearrange these blocks to form the palindrome ACACA (or CAAAC).
In total, she is able to answer "yes" to 3 of Bob's questions, so the answer is 3.
In Sample Case #2, N = 3 and Q = 5. For the first question, Anna must use the blocks XYZ to create a palindrome. This is impossible, and since the rest of Bob's questions are the same as the first one, the answer is 0.
"""
