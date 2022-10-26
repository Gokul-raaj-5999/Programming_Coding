class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()

        n, p, z = [], [], []
        for num in nums:
            if num > 0:
                p.append(num)
            elif num < 0: 
                n.append(num)
            else:
                z.append(num)

        N, P = set(n), set(p)

        if z:
            for num in P:
                if -1*num in N:
                    res.add((-1*num, 0, num))

        if len(z) >= 3:
            res.add((0,0,0))

        for i in range(len(n)):
            for j in range(i+1,len(n)):
                target = -1*(n[i]+n[j])
                if target in P:
                    res.add(tuple(sorted([n[i],n[j],target])))

        for i in range(len(p)):
            for j in range(i+1,len(p)):
                target = -1*(p[i]+p[j])
                if target in N:
                    res.add(tuple(sorted([p[i],p[j],target])))

        return res


# TLE ----------------------------------------------------------------
class Solution:
    def threeSum(self, a: List[int]) -> List[List[int]]:
        l = len(a)
        
        op = []
        
        for i in range(0, l):
            for j in range(i+1, l):
                for k in range(j+1, l):
                    if a[i] + a[j] + a[k] == 0:
                        x = [a[i], a[j], a[k]]
                        x.sort()
                        if x not in op:
                            op.append(x)


"""
15. 3Sum
Medium

22187

2031

Add to List

Share
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 

Constraints:

3 <= nums.length <= 3000
-105 <= nums[i] <= 105
"""
