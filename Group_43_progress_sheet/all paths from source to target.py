class Solution:
    def dfs(self, path, node, n):
        path.append(node)
        if node == n:
            self.paths.append(path.copy())
            path.pop()
            return
        
        for child in self.graph[node]:
            self.dfs(path, child, n)
        
        path.pop()
        

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.graph = graph
        self.paths = []
        for child in self.graph[0]:
            self.dfs([0], child, len(graph)-1)
        
        return self.paths
