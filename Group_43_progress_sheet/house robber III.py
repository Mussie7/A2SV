# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        @cache
        def dp(node, robbed_neigh):
            if not node:
                return 0
              
            money = dp(node.left, False) + dp(node.right, False)
            return money if robbed_neigh else max(dp(node.left, True) + dp(node.right, True) + node.val, money)
        
        return dp(root, False)
