# time complexity O(NlonN)-----------DP aproch----------------
class Solution:
    def longestPalindrome(self, s: str) -> str:
        l = len(s)
        dp = [ [False]*l for _ in range(l)]
        
        for i in range(l):
            dp[i][i] = True
            
        ans = s[0]
        for j in range(0, l):
            for i in range(0, j):
                if s[i] == s[j] and (dp[i+1][j-1] or j == i+1):
                    dp[i][j] = True
                    if j-i+1 > len(ans):
                        ans = s[i:j+1]
                        
        return ans
        
# TLE - O(N*2) -- but slow -----------------------------------
class Solution:
    def longestPalindrome(self, s: str) -> str:
        for i in range(0, l):
            ss = ''
            for j in range(i, l):
                ss += s[j]
                if ss == ss[::-1]:
                    op.append(ss)
        op.sort()
        # print(op)
        ms = ''
        mi = 0
        
        for i in op:
            if len(i) > mi:
                ms = i
                mi = len(i)
                # print(ms)
        return ms
        
        

"""
5. Longest Palindromic Substring
Medium

22169

1273

Add to List

Share
Given a string s, return the longest palindromic substring in s.

A string is called a palindrome string if the reverse of that string is the same as the original string.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
"""
