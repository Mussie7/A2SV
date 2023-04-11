# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node):
        if not node:
            return

        self.preorder_str.append(str(node.val))
        if not node.left and not node.right:
            return
        
        self.preorder_str.append('(')
        self.dfs(node.left)
        self.preorder_str.append(')')
        if node.right:
            self.preorder_str.append('(')
            self.dfs(node.right)
            self.preorder_str.append(')')

    def tree2str(self, root: Optional[TreeNode]) -> str:
        self.preorder_str = []
        self.dfs(root)
        return ''.join(self.preorder_str)
