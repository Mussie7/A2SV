# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def columnize(self, node, row, col):
        if not node:
            return
        
        self.columns[col].append((row, node.val))
        self.columnize(node.left, row + 1, col-1)
        self.columnize(node.right, row + 1, col+1)

    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.columns = defaultdict(list)
        self.columnize(root, 0, 0)

        columnOrder = []
        for key in sorted(self.columns.keys()):
            self.columns[key].sort(key = lambda x: x[1])
            self.columns[key].sort()
            columnOrder.append([val for row, val in self.columns[key]])
        
        return columnOrder
