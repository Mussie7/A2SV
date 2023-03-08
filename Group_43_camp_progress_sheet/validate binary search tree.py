# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode], lb = -inf, ub = inf) -> bool:
        if not root:
            return True

        if root.val <= lb or root.val >= ub:
            return False
        
        return self.isValidBST(root.left, lb, root.val) and self.isValidBST(root.right, root.val, ub)
