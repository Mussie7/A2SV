# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parent_map = {}
        que = deque([root])
        while que:
            node = que.popleft()
            if node.val == target.val:
                break
            
            if node.left:
                que.append(node.left)
                parent_map[node.left.val] = node
            if node.right:
                que.append(node.right)
                parent_map[node.right.val] = node
        
        visited = {target.val}
        que = deque([target])
        while k and que:
            for _ in range(len(que)):
                node = que.popleft()
                if node.left and node.left.val not in visited:
                    que.append(node.left)
                    visited.add(node.left.val)
                if node.right and node.right.val not in visited:
                    que.append(node.right)
                    visited.add(node.right.val)
                if node.val in parent_map and parent_map[node.val].val not in visited:
                    que.append(parent_map[node.val])
                    visited.add(parent_map[node.val].val)
            
            k -= 1
        
        return [node.val for node in que]
      
      
# if you decide to make a graph with the parents as possible childs
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def dfs(node):
            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
                dfs(node.left)
            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
                dfs(node.right)
        
        graph = defaultdict(list)
        dfs(root)
        que = deque([(target.val, -1)])
        while k and que:
            for _ in range(len(que)):
                node, parent = que.popleft()
                for neigh in graph[node]:
                    if neigh != parent:
                        que.append((neigh, node))
            k -= 1
        
        return [node[0] for node in que]
