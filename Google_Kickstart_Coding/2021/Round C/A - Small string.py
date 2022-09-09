MOD = 10**9+7

def smaller_strings():
    N, K = map(int, input().split())
    S = input()
    
    result = 0
    for i in range(0, (len(S)+1)//2):
        result = (result*K+(ord(S[i])-ord('a')))%MOD
        # print(result)
    for i in range((len(S)+1)//2, len(S)):
        if S[-1-i] != S[i]:
            result = (result+int(S[-1-i] < S[i]))%MOD
            break
        
    return result


for _ in range(0, int(input())):
    ans = smaller_strings()
    print (f'Case #{_+1}: {ans}')

"""

Smaller Strings (6pts, 9pts)

Practice Submissions
Attempt 3
S
check
check
Sep 3 2022, 11:08
remove_red_eye
Attempt 2
S
WA
remove_circle_outline
May 13 2022, 12:07
remove_red_eye
Attempt 1
S
WA
remove_circle_outline
May 13 2022, 12:05
remove_red_eye
Last updated: Sep 3 2022, 10:29

PROBLEM
ANALYSIS
Problem
You are given an integer K and a string S of length N, consisting of lowercase letters from the first K letters of the English alphabet. Find the number of palindrome strings of length N which are lexicographically smaller than S and consist of lowercase letters from the first K letters of the English alphabet.

A string composed of ordered letters a1,a2,…,an is lexicographically smaller than another string of the same length b1,b2,…,bn if ai<bi, where i is the first index where characters differ in the two strings. For example, the following strings are arranged in lexicographically increasing order: aaa, aab, aba, cab.

A palindrome is a string that is the same written forwards and backwards. For example, anna, racecar, aaa and x are all palindromes, while ab, frog and yoyo are not.

As the number of such strings can be very large, print the answer modulo 109+7.

Input
The first line of the input gives the number of test cases, T. T test cases follow.

Each test case consists of two lines. The first line contains two integers N and K. The second line contains a string S of length N, consisting of lowercase letters.

Output
For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the number of lexicographically smaller palindrome strings modulo 109+7.

Limits
Memory limit: 1 GB.
1≤T≤100.
The string S consists of lowercase letters from the first K letters of the English alphabet.
Test Set 1
Time limit: 20 seconds.
1≤N≤8.
1≤K≤5.
Test Set 2
Time limit: 10 seconds.
1≤N≤105.
1≤K≤26.
Sample
Sample Input
save_alt
content_copy
3
2 3
bc
5 5
abcdd
1 5
d
Sample Output
save_alt
content_copy
Case #1: 2
Case #2: 8
Case #3: 3
In Sample Case #1, the palindromes are ["aa", "bb"].

In Sample Case #2, the palindromes are ["aaaaa", "aabaa", "aacaa", "aadaa", "aaeaa", "ababa", "abbba", "abcba"].

In Sample Case #3, the palindromes are ["a", "b", "c"].
"""
