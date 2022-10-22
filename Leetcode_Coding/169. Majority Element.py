#time O(nlogn)
class Solution:
    def majorityElement(self, a: List[int]) -> int:
        dic = {}
        l = len(a)
        for i in range(0, len(a)):
            if a[i] in dic:
                dic[a[i]] += 1
            else:
                dic[a[i]] = 1
        b = []
        for i in dic:
            if dic[i] > l//2:
                b.append(i)
        b.sort()
        return b[-1]
        

"""
169. Majority Element
Easy

12378

397

Add to List

Share
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 

Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109
 """
