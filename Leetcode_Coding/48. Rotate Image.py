class Solution:
    def rotate(self, mat: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def rotate(A):
            N = len(A[0])
            for i in range(N // 2):
                for j in range(i, N - i - 1):
                    temp = A[i][j]
                    A[i][j] = A[N - 1 - j][i]
                    A[N - 1 - j][i] = A[N - 1 - i][N - 1 - j]
                    A[N - 1 - i][N - 1 - j] = A[j][N - 1 - i]
                    A[j][N - 1 - i] = temp
            return A
        return rotate(mat)
        


"""
48. Rotate Image
Medium

12681

593

Add to List

Share
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

 

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
Example 2:


Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
 

Constraints:

n == matrix.length == matrix[i].length
1 <= n <= 20
-1000 <= matrix[i][j] <= 1000
"""
