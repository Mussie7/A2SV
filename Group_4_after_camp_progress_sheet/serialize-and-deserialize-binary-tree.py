# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

        def dfs(node):
            if not node:
                str_tree.append('N/')
                return
            
            str_tree.append(str(node.val) + '/')
            dfs(node.left)
            dfs(node.right)

        
        str_tree = []
        dfs(root)
        return ''.join(str_tree)
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        tree = data.split('/')
        root = TreeNode(-inf)
        root.left = TreeNode(-inf)
        stack = [(root.left, root)]
        for i in range(len(tree) - 1):
            node, parent = stack.pop()
            if tree[i] == 'N':
                if node.val == -inf:
                    parent.left = None
                else:
                    parent.right = None
            else:
                node.val = int(tree[i])
                node.left = TreeNode(-inf)
                node.right = TreeNode(inf)
                stack.append((node.right, node))
                stack.append((node.left, node))
        
        return root.left


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))