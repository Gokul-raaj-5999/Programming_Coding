# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        
        if root is None:
            return result
        
        buf = [root]
        while len(buf):
            nodes = []
            lavel = []
            while len(buf):
                cur = buf.pop(0)
                lavel.append(cur.val)
                if (cur.left):
                    nodes.append(cur.left)
                if (cur.right):
                    nodes.append(cur.right)
            result.append(lavel)
            buf = nodes
        return result
                
        

"""
102. Binary Tree Level Order Traversal
Medium

11298

214

Add to List

Share
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000
"""
