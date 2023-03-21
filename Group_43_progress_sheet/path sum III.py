# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node, preSum, target):
        if not node:
            return 0
        
        preSum += node.val
        cur = self.preSumDic[preSum-target]

        self.preSumDic[preSum] += 1
        cur += self.dfs(node.left, preSum, target) + self.dfs(node.right, preSum, target)

        self.preSumDic[preSum] -= 1
        preSum -= node.val

        return cur

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.preSumDic = Counter([0])
        return self.dfs(root, 0, targetSum)
