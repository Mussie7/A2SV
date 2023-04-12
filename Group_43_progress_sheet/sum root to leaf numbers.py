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
            self.totalOfNums += int(path)
        
        if node.left:
            self.getRootLeafNums(path, node.left)

        if node.right:
            self.getRootLeafNums(path, node.right)

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.totalOfNums = 0
        self.getRootLeafNums('', root)
        return self.totalOfNums
