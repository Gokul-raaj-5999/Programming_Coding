class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        n = numRows
        op = [[1], [1,1]]
        if(n == 1):
            return([[1]])
        elif(n==2):
            return(op)
        else:
            for _ in range(3, n+1):
                vec = op[-1]
                tem = [1]
                for i in range(0, len(vec)-1):
                    tem.append(vec[i]+vec[i+1])
                tem.append(1)
                op.append(tem)
                
            print(op)
        return(op)
            


"""
118. Pascal's Triangle
Easy

7141

232

Add to List

Share
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]
 

Constraints:

1 <= numRows <= 30
Accepted
929,120
Submissions
1,377,550

Runtime: 28 ms, faster than 97.08% of Python3 online submissions for Pascal's Triangle.
Memory Usage: 14 MB, less than 17.88% of Python3 online submissions for Pascal's Triangle.
"""
