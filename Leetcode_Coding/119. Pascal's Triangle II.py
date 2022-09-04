class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        n = rowIndex
        op = [[1], [1,1]]
        if(n == 0):
            return([1])
        elif(n==1):
            return(op[-1])
        else:
            for _ in range(2, n+1):
                vec = op[-1]
                tem = [1]
                for i in range(0, len(vec)-1):
                    tem.append(vec[i]+vec[i+1])
                tem.append(1)
                op.append(tem)
                
            print(op)
        return(op[-1])
      
      

"""
119. Pascal's Triangle II
Easy

2911

273

Add to List

Share
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

Example 1:

Input: rowIndex = 3
Output: [1,3,3,1]
Example 2:

Input: rowIndex = 0
Output: [1]
Example 3:

Input: rowIndex = 1
Output: [1,1]
 

Constraints:

0 <= rowIndex <= 33
 

Follow up: Could you optimize your algorithm to use only O(rowIndex) extra space?

Accepted
561,619
Submissions
958,025

Runtime: 53 ms, faster than 36.43% of Python3 online submissions for Pascal's Triangle II.
Memory Usage: 14 MB, less than 16.36% of Python3 online submissions for Pascal's Triangle II.
"""
