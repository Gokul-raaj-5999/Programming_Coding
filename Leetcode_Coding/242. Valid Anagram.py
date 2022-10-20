class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a1 = []
        a2 = []
        for i in range(0, len(s)):
            a1.append(s[i])
        for i in range(0, len(t)):
            a2.append(t[i])
        a1.sort()
        a2.sort()
        if len(a1) != len(a2):
            return 0
        for i in range(0, len(a1)):
            if a1[i] != a2[i]:
                return 0
        else:
            return 1
        
                


"""
242. Valid Anagram
Easy

7244

242

Add to List

Share
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
"""
