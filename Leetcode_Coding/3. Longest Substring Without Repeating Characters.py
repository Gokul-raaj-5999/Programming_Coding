# time complexity O(n) sliding window optimized techiniqe 
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0
        # mp stores the current index of a character
        mp = {}

        i = 0
        # try to extend the range [i, j]
        for j in range(n):
            if s[j] in mp:
                i = max(mp[s[j]], i)

            ans = max(ans, j - i + 1)
            mp[s[j]] = j + 1

        return ans

#------------------------------------------------------------------
# time complexity O(n*2)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l = len(s)
        a = []
        for i in s:
            a.append(i)
        # print(a)
        
        i = 0
        maxarr = []
        while i < l:
            j = i
            seta = set()
            arr = []
            while j < l and len(seta) == len(arr):
                arr.append(s[j])
                seta.add(s[j])
                j+= 1
            maxarr.append(len(seta))
            i+= 1
        
        print(maxarr)
        if maxarr:
            return (max(maxarr))
        else:
            return 0
            

"""
3. Longest Substring Without Repeating Characters
Medium

29654

1259

Add to List

Share
Given a string s, find the length of the longest substring without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""
