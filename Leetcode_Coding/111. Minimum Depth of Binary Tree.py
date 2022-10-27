# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        res = []
        
        if root is None:
            return 0
        
        buf = [root]
        lc = 0
        while len(buf):
            node = []
            lev = []
            lc += 1
            while len(buf):
                cur = buf.pop(0)
                lev.append(cur.val)
                if cur.left:
                    node.append(cur.left)
                if cur.right:
                    node.append(cur.right)
                if  not cur.right and not cur.left:
                    return lc
            res.append(lev)
            buf = node
        return lc
                 

"""
111. Minimum Depth of Binary Tree
Easy

4985

1026

Add to List

Share
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 2
Example 2:

Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5
 

Constraints:

The number of nodes in the tree is in the range [0, 105].
-1000 <= Node.val <= 1000
"""
