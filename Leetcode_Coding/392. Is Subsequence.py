class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        print(s,t)
        i = 0
        j = 0
        count = 0
        if(len(s) > 0 and len(t) > 0):
            while(i < len(t) and j<len(s)):
                if(s[j]==t[i]):
                    j+=1
                    i+=1
                    count+=1
                else:
                    i+=1
                print(i,j)
            # print(count,len(s))
            if(count == len(s)):
                print('true')
                return(True)
            else:
                print('false')
                return(False)
        else:
            if(len(s)==0 and len(t) > 0 ):
                return(True)
            elif(len(s)==0 and len(t) == 0):
                return(True)
            else:
                return(False)
                
            
"""
Runtime: 80 ms, faster than 7.51% of Python3 online submissions for Is Subsequence.
Memory Usage: 14.2 MB, less than 8.41% of Python3 online submissions for Is Subsequence.

392. Is Subsequence
Easy

5305

310

Add to List

Share
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
 

Constraints:

0 <= s.length <= 100
0 <= t.length <= 104
s and t consist only of lowercase English letters.
 

Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109, and you want to check one by one to see if t has its subsequence. In this scenario, how would you change your code?
"""
