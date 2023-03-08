# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root.left and not root.right:
            return True
        
        elif (root.left and not root.right) or (root.right and not root.left) or (root.left.val != root.right.val):
            return False
        
        root.left.right, root.right.right = root.right.right, root.left.right
        return self.isSymmetric(root.left) and self.isSymmetric(root.right)
