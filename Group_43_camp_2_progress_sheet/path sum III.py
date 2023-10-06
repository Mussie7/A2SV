# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(node, curr_sum, target_sum):
            if not node:
                return 0

            curr_sum += node.val
            path_count = pre_sum_map[curr_sum - target_sum]
            pre_sum_map[curr_sum] += 1
            
            path_count += dfs(node.left, curr_sum, target_sum)
            path_count += dfs(node.right, curr_sum, target_sum)
            
            pre_sum_map[curr_sum] -= 1
            return path_count
        
        pre_sum_map = defaultdict(int)
        pre_sum_map[0] = 1
        return dfs(root, 0, targetSum)
