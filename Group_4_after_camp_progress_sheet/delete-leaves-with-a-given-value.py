# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return
                
            dfs(node.left)
            dfs(node.right)

            if node.left and not node.left.left and not node.left.right and node.left.val == target:
                node.left = None
            if node.right and not node.right.left and not node.right.right and node.right.val == target:
                node.right = None
        
        dummy = TreeNode(-1, left=root)
        dfs(dummy)
        return dummy.left
