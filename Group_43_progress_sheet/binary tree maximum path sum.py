# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node):
        if not node:
            return -1
        
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        cur_path_sum = max(0, left) + max(0, right) + node.val
        
        self.max_path_sum = max(cur_path_sum, self.max_path_sum)
        return node.val + max(0, left, right)

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_path_sum = -inf
        self.dfs(root)
        return self.max_path_sum
