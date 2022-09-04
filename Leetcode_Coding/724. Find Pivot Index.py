class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        l =  len(nums)
        sum = 0
        op = []
        for i in nums:
            sum += i
            op.append(sum)
        print(op)
        for i in range(0, len(op)):
            if i > 0:
                if op[i] == op[-1]-op[i-1]:
                    return i
            else:
                if op[i] == op[-1]:
                    return i
            
        else:
            return -1
                
            

"""
Success
Details 
Runtime: 177 ms, faster than 81.84% of Python3 online submissions for Find Pivot Index.
Memory Usage: 15.3 MB, less than 48.84% of Python3 online submissions for Find Pivot Index.
Next challenges:

724. Find Pivot Index
Easy

4489

493

Add to List

Share
Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.

 

Example 1:

Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The pivot index is 3.
Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
Right sum = nums[4] + nums[5] = 5 + 6 = 11
Example 2:

Input: nums = [1,2,3]
Output: -1
Explanation:
There is no index that satisfies the conditions in the problem statement.
Example 3:

Input: nums = [2,1,-1]
Output: 0
Explanation:
The pivot index is 0.
Left sum = 0 (no elements to the left of index 0)
Right sum = nums[1] + nums[2] = 1 + -1 = 0
 

Constraints:

1 <= nums.length <= 104
-1000 <= nums[i] <= 1000
 

Note: This question is the same as 1991: https://leetcode.com/problems/find-the-middle-index-in-array/
"""
