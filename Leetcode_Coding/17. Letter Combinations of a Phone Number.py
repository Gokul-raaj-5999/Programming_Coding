class Solution(object):
    def letterCombinations(self, digits):
        dic = { "2": "abc", "3": "def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        
        res=[]
        if len(digits) ==0:
            return res
            
        self.dfs(digits, 0, dic, '', res)
        return res
    
    def dfs(self, nums, index, dic, path, res):
        if index >=len(nums):
            res.append(path)
            return
        string1 =dic[nums[index]]
        for i in string1:
            self.dfs(nums, index+1, dic, path + i, res)

"""
17. Letter Combinations of a Phone Number
Medium

12999

769

Add to List

Share
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


 

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]
 

Constraints:

0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].
"""
