# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        def dfs(node):
            parent = [node.val]
            if not node.left:
                parent.append(None)
            else:
                parent.extend(dfs(node.left))
            
            if not node.right:
                parent.append(None)
            else:
                parent.extend(dfs(node.right))

            tup_parent = tuple(parent)
            if tup_parent in node_map:
                node_map[tup_parent] += 1
                if node_map[tup_parent] == 2:
                    duplicates.append(node)
            else:
                node_map[tup_parent] = 1
            
            return parent
        
        node_map = {}
        duplicates = []
        dfs(root)
        return duplicates

    # P.S. a better implementation would be using string
    def dfs(self, node, nodes, duplicates):
        if not node:
            return 'n'
        
        str_node = str(node.val) + '-' + self.dfs(node.left, nodes, duplicates) + '-' + self.dfs(node.right, nodes, duplicates)
        
        nodes[str_node] += 1
        if nodes[str_node] == 2:
            duplicates.add(node)        
        
        return str_node

    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        duplicates = set()
        self.dfs(root, Counter(), duplicates)
        return duplicates
