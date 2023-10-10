# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node, level, number):
            nonlocal max_width
            if not node:
                return

            if level in level_map:
                max_width = max(max_width, number + 1 - level_map[level])
            else:
                level_map[level] = number
            
            dfs(node.left, level + 1, 2 * number)
            dfs(node.right, level + 1, 2 * number + 1)
        
        
        level_map = {0: 0}
        max_width = 0
        dfs(root, 0, 0)
        return max_width
