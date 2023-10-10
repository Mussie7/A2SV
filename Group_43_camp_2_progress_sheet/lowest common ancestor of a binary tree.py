# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node):
            nonlocal ans
            if not node:
                return False
                        
            left = dfs(node.left)
            right = dfs(node.right)
            if (left and right) or ((left or right) and (node == p or node == q)):
                ans = node

            return left or right or node == p or node == q

        ans = None
        dfs(root)
        return ans
