class Solution:
    def gameOfLife(self, lst: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        m = len(lst)
        n = len(lst[0])
        
        def calcul(rpos):
            zero = 0
            one = 0
            for i,j in rpos:
                if i >= 0 and i < m and j>= 0 and j < n:
                    if lst[i][j] == 0:
                        zero += 1
                    else:
                        one += 1
            return zero, one
                
        def rule(cur, z, o):
            if cur == 1 and o < 2: return 0
            elif cur == 1 and (o == 2 or o == 3): return 1
            elif cur == 1 and z > 3: return 0
            elif cur == 0 and o == 3: return 1
            else:
                return 0
                   
        mat = []
        for i in range(0, m):
            x = []
            for j in range(0, n):
                print(lst[i][j], end = '-')
                rpos = [ [i-1,j-1], [i-1,j], [i-1,j+1], [i,j-1], [i,j+1], [i+1,j-1], [i+1,j], [i+1,j+1] ]
                z, o =   calcul(rpos)
                req = rule(lst[i][j], z, o)
                print(req, end = ' ')
                x.append(req)
            mat.append(x)
            print()
            
        print()
        for i in mat:
            print(i)
            
        for i in range(0, m):
            for j in range(0, n):
                lst[i][j] = mat[i][j]
            
                
        
        
        

"""
289. Game of Life
Medium

5278

464

Add to List

Share
According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population.
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.

 

Example 1:


Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
Example 2:


Input: board = [[1,1],[1,0]]
Output: [[1,1],[1,1]]
 

Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 25
board[i][j] is 0 or 1.
 

Follow up:

Could you solve it in-place? Remember that the board needs to be updated simultaneously: You cannot update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches upon the border of the array (i.e., live cells reach the border). How would you address these problems?
"""
