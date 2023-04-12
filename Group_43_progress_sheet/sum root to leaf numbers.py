# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getRootLeafNums(self, path, node):
        path += str(node.val)
        if not node.left and not node.right:
            return int(path)
        
        if not node.left:
            return self.getRootLeafNums(path, node.right)

        if not node.right:
            return self.getRootLeafNums(path, node.left)
        
        return self.getRootLeafNums(path, node.left) + self.getRootLeafNums(path, node.right)

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return self.getRootLeafNums('', root)
