# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        que = deque([[root, 1]])
        max_width = 1
        while que:
            cur_level = [] 
            for _ in range(len(que)):
                node, num = que.popleft()
                if node.left:
                    cur_level.append([node.left, num * 2 - 1])
                if node.right:
                    cur_level.append([node.right, num * 2])
            
            if len(cur_level) > 1:
                max_width = max(max_width, cur_level[-1][1] - cur_level[0][1] + 1)
            que = deque(cur_level)
        
        return max_width
