# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getRightSideView(self, node, level):
        if not node:
            return
        
        if level > len(self.rightView):
            self.rightView.append(node.val)
        else:
            self.rightView[level-1] = node.val

        self.getRightSideView(node.left, level + 1)
        self.getRightSideView(node.right, level + 1)

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.rightView = []
        self.getRightSideView(root, 1)
        return self.rightView
