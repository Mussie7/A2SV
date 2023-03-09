# iterative
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

# recursive
class Solution:
    def dfs(self, node, level, num):
        if not node:
            return

        if level in self.levelDict:
            self.max_width = max(self.max_width, num - self.levelDict[level] + 1)
        else:
            self.levelDict[level] = num
        
        self.dfs(node.left, level+1, num * 2 - 1)
        self.dfs(node.right, level+1, num * 2)

    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.levelDict = {}
        self.max_width = 1
        self.dfs(root, 1, 1)
        return self.max_width
