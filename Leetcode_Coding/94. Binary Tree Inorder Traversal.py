# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if not root: return
        
        def inorder(node):
            if not node:
                return
            
            inorder(node.left)
            ans.append(node.val)
            inorder(node.right)
        
        inorder(root)
        return ans
            

"""
94. Binary Tree Inorder Traversal
Easy

9700

460

Add to List

Share
Given the root of a binary tree, return the inorder traversal of its nodes' values.

 

Example 1:


Input: root = [1,null,2,3]
Output: [1,3,2]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]
 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
"""
