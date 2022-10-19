class Solution:
    def firstUniqChar(self, s: str) -> int:
        alp = [[-1,0, '-']]*26
        print(alp)
        l = len(s)
        for i in range(0, l):
            pos = ord(s[i]) - 97
            if alp[pos][1] == 0:
                alp[pos] = [i, 1,s[i]]
            elif alp[pos][1] == 1:
                alp[pos] = [-1, 2, '*']
        alp.sort()
        print(alp)
        for i in range(0, len(alp)):
            if alp[i][0] != -1:
                print(alp[i][0])
                return alp[i][0]
        else:
            return -1
          
          
"""
387. First Unique Character in a String
Easy

6832

231

Add to List

Share
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 

Example 1:

Input: s = "leetcode"
Output: 0
Example 2:

Input: s = "loveleetcode"
Output: 2
Example 3:

Input: s = "aabb"
Output: -1
 

Constraints:

1 <= s.length <= 105
s consists of only lowercase English letters.
"""
