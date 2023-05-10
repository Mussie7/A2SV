from typing import List
class Solution:
    #Function to detect cycle in an undirected graph.
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        def dfs(node, parent):
            visited[node] = 1
            for child in adj[node]:
                if visited[child] == 2 or child == parent:
                    continue
                if visited[child] == 1 or not dfs(child, node):
                    return False
            
            visited[node] = 2        
            return True
            
        visited = [0] * V
        for i in range(V):
            if visited[i] == 0:
                if not dfs(i, -1):
                    return True
        
        return False
