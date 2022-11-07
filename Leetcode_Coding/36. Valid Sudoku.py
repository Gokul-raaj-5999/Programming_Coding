#--------time complexity---- most optimised code------------
class Solution:
    def isValidSudoku(self, mat: List[List[str]]) -> bool:
        row = [set() for x in range(9)]
        col = [set() for x in range(9)]
        squ = [[set() for x in range(3)] for y in range(3)]

        for x in range(9):
            for y in range(9):
                cur = mat[x][y]
                if cur == '.':
                    continue
                elif cur in row[x] or cur in col[y] or cur in squ[x//3][y//3]:
                    return False
                else:
                    row[x].add(cur)
                    col[y].add(cur)
                    squ[x//3][y//3].add(cur)
        return True
        
#-----------pure logic and more time ----------------------------- 
class Solution:
    def isValidSudoku(self, mat: List[List[str]]) -> bool:
        
        for i in range(0, 9):
            s = set()
            c = 0
            for j in range(0, 9):
                if mat[i][j] != '.':
                    s.add(int(mat[i][j]))
                    c += 1
                if len(s) != c:
                    print('1')
                    return False
        
        for j in range(0, 9):
            s = set()
            c = 0
            for i in range(0, 9):
                if mat[i][j] != '.':
                    s.add(int(mat[i][j]))
                    c += 1
                if len(s) != c:
                    print('2')
                    return False
        c = 0
        lst = [[0,0], [0,3], [0,6], 
               [3,0], [3,3], [3,6],
               [6,0], [6,3], [6,6]]
        for ii, jj in lst:
            i = ii
            s = set()
            c = 0
            while i < ii+3:
                j = jj
                while j < jj+3:
                    print(i,'-', j, end = ' ')
                    if mat[i][j] != '.':
                        s.add(mat[i][j])
                        c += 1
                    if len(s) != c:
                        return False
                    j += 1
                print(s, c)
                i += 1
            print()
        return True
       

"""
36. Valid Sudoku
Medium
6.8K
815
Companies
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
 

Example 1:


Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
Example 2:

Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
 

Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit 1-9 or '.'.
"""
