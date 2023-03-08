# iterative solution
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = [root]
        count = 0
        while stack:
            node = stack.pop()
            if not node.left and not node.right:
                count += 1
                if count == k:
                    return node.val
                continue
            
            if node.right:
                stack.append(node.right)
            left = node.left
            node.right = None
            node.left = None

            stack.append(node)
            if left:
                stack.append(left)

# recursive solution
class Solution:
    def findKthElement(self, node, k, count):
        if not node:
            return count
        
        count = self.findKthElement(node.left, k, count) + 1
        if count == k:
            self.kthElement = node.val
            return count
        return self.findKthElement(node.right, k, count) 

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.kthElement = None
        self.findKthElement(root, k, 0)
        return self.kthElement
