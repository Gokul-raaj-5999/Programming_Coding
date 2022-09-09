import math

def fact(num) :
    i = 1
    count = 0
    while(i <= math.sqrt(num)):
        if (num % i == 0) :
            if (num / i == i) :
                s = str(i)
                if(s==s[::-1]):
                    count+=1
            else :
                ii = int(num/i)
                s = str(i)
                ss = str(ii)
                if(s==s[::-1]):
                    count+=1
                if(ss==ss[::-1]):
                    count+=1

        i = i + 1
    return(count)

for x in range (0, int(input())):
    a = int(input())
    ans = fact(a)
    print(f"Case #{x+1}: {ans}")
    

"""

Palindromic Factors (6pts, 9pts)

Attempts

1

Penalties

0

Penalty Time

00:55:52

Points

done
Points

done
Practice Submissions
You have not attempted this problem.
Submissions
Attempt 1
S
check
check
00:55:52
remove_red_eye
Last updated: Aug 31 2022, 19:03

PROBLEM
ANALYSIS
Problem
You are given a positive integer A. Find the number of factors of A which are palindromes. A number is called a palindrome if it remains the same when the digits in decimal representation are reversed. For instance, 121 is a palindrome, while 123 is not.

Input
The first line of the input gives the number of test cases, T. T lines follow.

Each line represents a test case and contains a single integer A.

Output
For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the number of factors of A which are palindromes.

Limits
Time limit: 2 seconds.
Memory limit: 1 GB.
1≤T≤100.
Test Set 1
1≤A≤103.
Test Set 2
1≤A≤1010.
Sample
Sample Input
save_alt
content_copy
4
6
10
144
242
Sample Output
save_alt
content_copy
Case #1: 4
Case #2: 3
Case #3: 7
Case #4: 6
In the first test case, A has 4 factors which are palindromes: 1,2,3, and 6.
In the second test case, A has 3 factors which are palindromes: 1,2, and 5.
In the third test case, A has 7 factors which are palindromes: 1,2,3,4,6,8, and 9.
In the fourth test case, A has 6 factors which are palindromes: 1,2,11,22,121, and 242.
"""
