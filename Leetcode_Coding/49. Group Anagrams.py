class Solution:
    def groupAnagrams(self, a: List[str]) -> List[List[str]]:
        
        def func(s):
            l = len(s)
            arr = []
            for i in s:
                arr.append(i)
            arr.sort()
            x = ''.join(x for x in arr)
            return x
        
        b = []
        dic = {}
        
        for i in a:
            x = func(i)
            b.append(x)
            
        for i in range(0, len(a)):
            ele , sele = a[i], b[i]
            if sele in dic:
                dic[sele].append(ele)
            else:
                dic[sele] = [ele]
            
        print(dic)
        op = []
        for i in dic:
            op.append(dic[i])
        return op
            
       
"""
49. Group Anagrams
Medium

12544

378

Add to List

Share
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""
