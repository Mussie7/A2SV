# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preOrder(self, node, level):
        if not node:
            return
        
        if level > len(self.levelNodes):
            self.levelNodes.append([node.val])
        else:
            self.levelNodes[level-1].append(node.val)
        
        self.preOrder(node.left, level+1)
        self.preOrder(node.right, level+1)

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.levelNodes = []
        self.preOrder(root, 1)
        return self.levelNodes
