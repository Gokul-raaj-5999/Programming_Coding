#---------time complexicity  O(longN)----------------------
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary(arr, x):
            s = 0
            e = len(arr)-1
            m = (s+e)//2
            while s <= e:
                m = (s+e)//2
                if x == arr[m]:
                    return m
                elif x < arr[m]:
                    e = m-1
                elif x > arr[m]:
                    s = m+1
            return -1

        a = [-1,-1]
        if len(nums) == 0:
            return a
        elif len(nums) == 1 and nums[0] == target:
            return [0,0]
        elif len(nums) == 1 and nums[0] != target:
            return a
        ind= binary(nums, target)
        print(ind)
        if ind == -1:
            return a
        for i in range(ind, -1, -1):
            if nums[i] == target:
                a[0] = i
        print(a)
        for i in range(ind, len(nums)):
            if nums[i] == target:
                a[1] = i
        print(a)
        return a
      
#-------------------Time complex code O(N)---------------------------
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary(arr, x):
          a = [-1, -1]
          for i in range(0, len(nums)):
              if nums[i] == target and a[0] == -1:
                  a[0] = i
              if nums[i] == target and a[0] != -1:
                  a[1] = i
          return a





"""
34. Find First and Last Position of Element in Sorted Array
Medium
14.6K
355
Companies
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109
"""
