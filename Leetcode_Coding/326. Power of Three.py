#faster solution 
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return (n > 0) and 1162261467 % n == 0
      
      
      
#slower solution
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        x = 0
        a = [1]
        
        while 3**x < n:
            x += 1
            a.append(3**x)
        print(a)
        if a[-1] == n:
            return True
        else:
            return False
        
        

"""
326. Power of Three
Easy

2142

205

Add to List

Share
Given an integer n, return true if it is a power of three. Otherwise, return false.

An integer n is a power of three, if there exists an integer x such that n == 3x.

 

Example 1:

Input: n = 27
Output: true
Explanation: 27 = 33
Example 2:

Input: n = 0
Output: false
Explanation: There is no x where 3x = 0.
Example 3:

Input: n = -1
Output: false
Explanation: There is no x where 3x = (-1).
 

Constraints:

-231 <= n <= 231 - 1
"""
