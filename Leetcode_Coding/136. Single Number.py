class Solution:
    def singleNumber(self, a: List[int]) -> int:
        a.sort()
        for i in range(0, len(a)-1, 2):
            if a[i] != a[i+1]:
                return a[i]
        else:
            return a[-1]
                
        

"""
136. Single Number
Easy

11828

450

Add to List

Share
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 

Example 1:

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4
Example 3:

Input: nums = [1]
Output: 1
 

Constraints:

1 <= nums.length <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
Each element in the array appears twice except for one element which appears only once.
"""
