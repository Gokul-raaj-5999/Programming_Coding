for x in range(1, int(input())+1):
    s = "IMPOSSIBLE"
    I = str(input())
    P = str(input())
    li = len(I)
    lp = len(P)
    a = 0
    if(li>lp):
        count = 0
    else:
        i = 0
        j = 0
        count = 0
        ans = 0
        while(i<li and j<lp):
            if(I[i]==P[j]):
                    i+=1
                    j+=1
                    count +=1
            else:
                j+=1
                ans+=1
        
    if(count==li):
        ans = ans + lp - j
        print(f"Case #{x}: {ans}")
    else:
        print(f"Case #{x}: {s}")

"""

Speed Typing (5pts, 9pts)

Practice Submissions
Attempt 2
S
check
check
Apr 22 2022, 21:44
remove_red_eye
Attempt 1
S
WA
remove_circle_outline
Apr 22 2022, 20:59
remove_red_eye
Last updated: Aug 31 2022, 19:06

PROBLEM
ANALYSIS
Problem
Barbara is a speed typer. In order to check her typing speed, she performs a speed test. She is given a string I that she is supposed to type.

While Barbara is typing, she may make some mistakes, such as pressing the wrong key. As her typing speed is important to her, she does not want to spend additional time correcting the mistakes, so she continues to type with the errors until she finishes the speed test. After she finishes the speed test, she produces a P.

Now she wonders how many extra letters she needs to delete in order to get I from P. It is possible that Barbara made a mistake and P cannot be converted back to I just by deleting some letters. In particular, it is possible that Barbara missed some letters.

Help Barbara find out how many extra letters she needs to remove in order to obtain I or if I cannot be obtained from P by removing letters then output IMPOSSIBLE.

Input
The first line of the input gives the number of test cases, T. T test cases follow.

Each test case has 2 lines. The first line of each test case is an input string I (that denotes the string that the typing test has provided). The next line is the produced string P (that Barbara has entered).

Output
For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the number of extra letters that need to be removed in order to obtain I. If it is not possible to obtain I then output IMPOSSIBLE as y.

Limits
Memory limit: 1 GB.
1≤T≤100.
Both the strings contain letters from a-z and A-Z.
Length of the given strings will be 1≤|I|,|P|≤105.
Test Set 1
Time limit: 20 seconds.
All letters in I are the same.

Test Set 2
Time limit: 40 seconds.
Sample
Note: there are additional samples that are not run on submissions down below.
Sample Input
save_alt
content_copy
2
aaaa
aaaaa
bbbbb
bbbbc
Sample Output
save_alt
content_copy
Case #1: 1
Case #2: IMPOSSIBLE
In the first test case, P contains one extra a, so she needs to remove 1 extra letter in order to obtain I.
In the second test case, Barbara typed only 4 letters b, while I consists of 5 letters b so the answer is IMPOSSIBLE.


Additional Sample - Test Set 2
The following additional sample fits the limits of Test Set 2. It will not be run against your submitted solutions.
Sample Input
save_alt
content_copy
2
Ilovecoding
IIllovecoding
KickstartIsFun
kkickstartiisfun
Sample Output
save_alt
content_copy
Case #1: 2
Case #2: IMPOSSIBLE
In the first test case, P has 2 extra letters, I and l. The other letters are in the order given in I. So she needs to remove 2 letters in order to obtain I.
In the second test case, there is no letter K in P so the answer is IMPOSSIBLE.
"""
