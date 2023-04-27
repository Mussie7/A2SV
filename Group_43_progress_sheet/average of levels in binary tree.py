# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        que = deque([(0, root)])
        level_sum = []
        while que:
            level, node = que.popleft()
            if level < len(level_sum):
                level_sum[level][0] += node.val
                level_sum[level][1] += 1
            else:
                level_sum.append([node.val, 1])
            
            if node.left:
                que.append((level + 1, node.left))
            if node.right:
                que.append((level +1, node.right))
        
        for i, (level, count) in enumerate(level_sum):
            level_sum[i] = level / count
        
        return level_sum
