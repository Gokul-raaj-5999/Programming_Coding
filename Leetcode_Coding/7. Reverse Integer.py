class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        n = int(X)
        
        if s[0] == '-':
            s = s[1:]
            s = s[::-1]
            n = int(s)
            if n >= 2147483648:
                return 0
            s = '-'+ str(n)
            return s
        else:
            s = s[::-1]
            n = int(s)
            if n >= 2147483648 -1:
                return 0
            return n
            
        


"""
7. Reverse Integer
Medium

8778

10920

Add to List

Share
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
 

Constraints:

-231 <= x <= 231 - 1
"""
