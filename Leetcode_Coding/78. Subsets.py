from itertools import combinations 

class Solution:
    def subsets(self, a: List[int]) -> List[List[int]]:
        op = []
        
        for i in range(0, len(a)+1):
            x = combinations(a, i)
            op.extend(x)
        return op
        
                
            
                

"""
78. Subsets
Medium

12544

181

Add to List

Share
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
 

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.
"""
