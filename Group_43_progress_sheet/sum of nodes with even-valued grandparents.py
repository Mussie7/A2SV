# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        
        def dfs(node):
            if not node:
                return
            
            nonlocal total
            if not node.val % 2 and node.left:
                if node.left.left:
                    total += node.left.left.val
                
                if node.left.right:
                    total += node.left.right.val
            
            if not node.val % 2 and node.right:
                if node.right.left:
                    total += node.right.left.val
                
                if node.right.right:
                    total += node.right.right.val
            
            dfs(node.left)
            dfs(node.right)
        
        total = 0
        dfs(root)
        
        return total
