# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def dfs(node, curr_values, curr_values_sum):
            curr_values.append(node.val)
            curr_values_sum += node.val

            if not node.left and not node.right:
                if curr_values_sum == targetSum:
                    value_paths.append(curr_values.copy())
                # can't forget to pop when returning
                curr_values.pop()
                return
            
            if node.left:
                dfs(node.left, curr_values, curr_values_sum)
            if node.right:
                dfs(node.right, curr_values, curr_values_sum)

            curr_values.pop()
            return

        if not root:
            return []

        value_paths = []
        dfs(root, [], 0)
        return value_paths
