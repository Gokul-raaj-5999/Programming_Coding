class Solution:
    def countBits(self, n: int) -> List[int]:
        ar = [0,1,1,2]
        if(n < len(ar)):
            return(ar[:n+1])
        else:
            for num in range(4,n+1):
                one = 1 if num%2!=0 else 0
                one += ar[num//2]
                ar.append(one)
            return(ar[:n+1])
                
                


"""
Runtime: 157 ms, faster than 40.92% of Python3 online submissions for Counting Bits.
Memory Usage: 20.8 MB, less than 78.91% of Python3 online submissions for Counting Bits.

338. Counting Bits
Easy

7401

347

Add to List

Share
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

 

Example 1:

Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10
Example 2:

Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101
 

Constraints:

0 <= n <= 105
 

Follow up:

It is very easy to come up with a solution with a runtime of O(n log n). Can you do it in linear time O(n) and possibly in a single pass?
Can you do it without using any built-in function (i.e., like __builtin_popcount in C++)?
Accepted
625,327
Submissions
836,591
"""
