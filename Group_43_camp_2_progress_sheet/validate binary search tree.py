# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validator(node, ub, lb):
            if not node:
                return True
            
            if not lb < node.val < ub:
                return False
            
            return validator(node.left, node.val, lb) and validator(node.right, ub, node.val)
        
        return validator(root, math.inf, -math.inf)
