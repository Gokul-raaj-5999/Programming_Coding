class Solution:
    def intersect(self, a: List[int], b: List[int]) -> List[int]:
        if len(a) < len(b): #b in a by default keep a as big
            a, b = b, a
        l1 = len(a)
        l2 = len(b)
        m = []
        
        a.sort()
        b.sort()
        
        i = 0
        j = 0
        f = 1
        m = []
        while i < l1 and j < l2 and f:
            if a[i] == b[j]:
                m.append(a[i])
                i += 1
                j += 1
            else:
                if a[i] > b[j]:
                    j += 1
                else:
                    i += 1
        return m
              
        

"""
350. Intersection of Two Arrays II
Easy

5471

788

Add to List

Share
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

 

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.
 

Constraints:

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000
"""
