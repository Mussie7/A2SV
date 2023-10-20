# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return [0, 0]
            
            left_coins, left_dist = dfs(node.left)
            right_coins, right_dist = dfs(node.right)

            # count of coins at this node is the total of the amount from left, right and on this node
            # negative coins means coins need to come this way
            # positive coins means coins need to leave this node
            count = (node.val - 1) + left_coins + right_coins

            # the travel distance of the coins is the sum of the distance already traveled and the count of coins that are going to travel one time from/to this node
            totalDist = left_dist + right_dist + abs(count)  
            return [count, totalDist]
        return dfs(root)[1]
