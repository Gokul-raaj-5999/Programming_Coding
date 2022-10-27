class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def call(left, right, s):
            if len(s) == 2*n:
                res.append(s)
                return 
            
            if left < n:
                call(left+1, right, s+ '(')
            if right < left:
                call(left, right+1, s+ ')' )
            
        call (0, 0, '' )
        return res
                
                

"""
22. Generate Parentheses
Medium

15674

602

Add to List

Share
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
 

Constraints:

1 <= n <= 8
"""
