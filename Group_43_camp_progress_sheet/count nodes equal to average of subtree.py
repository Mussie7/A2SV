# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAverage(self, node):
        if not node:
            return 0, 0, 0
        
        left = self.getAverage(node.left)
        right = self.getAverage(node.right)

        total_nodes = left[0] + right[0] + 1
        total_nodes_sum = node.val + left[1] + right[1]
        average_nodes = left[2] + right[2]
        if total_nodes_sum // total_nodes == node.val:
            average_nodes += 1
        
        return total_nodes, total_nodes_sum, average_nodes

    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        return self.getAverage(root)[2]
