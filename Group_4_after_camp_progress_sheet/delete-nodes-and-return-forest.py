# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        def dfs(node, parent):
            if not node:
                return
            
            if node.val in to_delete_set:
                if parent and parent.left == node:
                    parent.left = None
                elif parent and parent.right == node:
                    parent.right = None
                
                dfs(node.left, None)
                dfs(node.right, None)
                return
            
            if not parent:
                forest.append(node)
            
            dfs(node.left, node)
            dfs(node.right, node)
            return



        forest = []
        to_delete_set = set(to_delete)
        dfs(root, None)
        return forest