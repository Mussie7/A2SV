# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, ub=inf):
        root = TreeNode(self.preorder[self.index])
        self.index += 1
        
        if self.index < len(self.preorder) and self.preorder[self.index] < root.val:
            root.left = self.dfs(root.val)
        
        if self.index < len(self.preorder) and self.preorder[self.index] < ub:
            root.right = self.dfs(ub)
        
        return root

    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        self.preorder = preorder
        self.index = 0
        return self.dfs()
