#-----------optmised solution -------------
class Solution(object):
    def strStr(self, haystack, needle):
        return haystack.find(needle)
      
      
#-----------normal solution ----------------
class Solution:
    def strStr(self, a: str, b: str) -> int:
        f = -1
        l1 = len(a)
        l2 = len(b)
        for i in range(0, l1):
            if a[i:i+l2] == b:
                f = i
                return f
        return f

"""
28. Find the Index of the First Occurrence in a String
Medium
852
66
Companies
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
 

Constraints:

1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.
"""
