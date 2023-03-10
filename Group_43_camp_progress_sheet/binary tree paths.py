# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathFinder(self, node, path):
        if not node.left and not node.right:
            self.paths.append(''.join(path) + str(node.val))
            return
        
        if node.left:
            path.append(str(node.val) + '->')
            self.pathFinder(node.left, path)
            path.pop()
        
        if node.right:
            path.append(str(node.val) + '->')
            self.pathFinder(node.right, path)
            path.pop()

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.paths = []
        self.pathFinder(root, [])
        return self.paths
