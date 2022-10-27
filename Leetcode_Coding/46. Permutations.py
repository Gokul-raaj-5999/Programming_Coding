class Solution:
    def permute(self, n: List[int]) -> List[List[int]]:
        
        def backtrack(vis, ans, d, n):
            if len(d) == len(n):
                ans.append(d.copy())
                return 
            
            for i in range (len(n)):
                if not vis[i]:
                    vis[i] = True
                    d.append(n[i])
                    backtrack(vis, ans, d, n)
                    d.pop()
                    vis[i] = False     

        
        vis = [False]*len(n)
        ans,d  = [], []
        
        backtrack(vis, ans, d, n)
        
        return ans
        


"""
46. Permutations
Medium

13471

225

Add to List

Share
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]
 

Constraints:

1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.
"""
