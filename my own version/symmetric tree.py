# It took 40 minutes and 2 tries


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        q, stack = deque(), []
        q.append(root)
        stack.append(root)
        count, n = 1, 1

        while q:    
            if count == n:
                count = 0
                for i in range(n):
                    node = q.popleft()

                    if stack and stack[-1] and node and stack[-1].val == node.val:
                        stack.pop()
                    elif stack and not stack[-1] and node == None:
                        stack.pop()
                    else:
                        return False

                    if node:
                        q.append(node.left)
                        q.append(node.right)

                    if i == n-1:
                        n = len(q) // 2
            else:
                node = q.popleft()
                stack.append(node)
                
                if node:
                    q.append(node.left)
                    q.append(node.right)
                
                count += 1

        return not stack
