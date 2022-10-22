class Solution:
    def getSum(self, a: int, b: int) -> int:
        op = []
        if a >= 0 and b >= 0:
            for i in range(0, a):
                op.append(i)
            for i in range(0, b):
                op.append(i)
                
            ans = len(op)
        elif (a > 0 and b < 0):
            if abs(b) > a:
                for i in range(0, abs(b)):
                    op.append(0)
                for i in range(0, a):
                    op.pop(0)
                    
                    ans = -len(op)
            else:
                for i in range(0, a):
                    op.append(0)
                for i in range(0, abs(b)):
                    op.pop(0)
                
                ans = len(op)
            
        elif (a < 0 and b >0):
            if abs(a) > b:
                for i in range(0, abs(a)):
                    op.append(0)
                for i in range(0, b):
                    op.pop(0)
                
                ans = -len(op)
            else:
                for i in range(0, b):
                    op.append(0)
                for i in range(0, abs(a)):
                    op.pop(0)
                ans = len(op)
            
        else:
            a = abs(a)
            b = abs(b)
            for i in range(0, a):
                op.append(i)
            for i in range(0, b):
                op.append(i)
                
            ans = -len(op)
            
        
            
        return ans
        


"""
371. Sum of Two Integers
Medium

3092

4385

Add to List

Share
Given two integers a and b, return the sum of the two integers without using the operators + and -.

 

Example 1:

Input: a = 1, b = 2
Output: 3
Example 2:

Input: a = 2, b = 3
Output: 5
 

Constraints:

-1000 <= a, b <= 1000
"""
