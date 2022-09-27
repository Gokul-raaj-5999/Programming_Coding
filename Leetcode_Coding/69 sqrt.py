class Solution:
    def mySqrt(self, x: int) -> int:
        def binary(x):
            s = 2
            e = x//2+1
            mid = (e+s)//2
            while s <=e:
                mid = (e+s)//2
                
                if mid*mid == x:
                    return(mid)
                elif mid*mid > x:
                    e = mid-1
                elif mid*mid < x:
                    s = mid + 1
            if mid*mid > x:
                mid -=1
            return mid
                    
        x = x
        a= []
        if x == 1:
            return 1
        elif x == 0:
            return 0
        else:
            num = binary(x)
            return (num)
        
        
        

"""
69. Sqrt(x)
Easy

4890

3558

Add to List

Share
Given a non-negative integer x, compute and return the square root of x.

Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.

Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.

 

Example 1:

Input: x = 4
Output: 2
Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned."""
