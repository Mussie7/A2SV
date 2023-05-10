class Solution:
    def dfs(self, node):
        self.visited[node] = 1
        for neigh in self.graph[node]:
            if self.visited[neigh] == 2:
                continue
            if self.visited[neigh] == 1 or not self.dfs(neigh):
                return False
        
        self.visited[node] = 2
        return True

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        self.graph = graph
        self.n = len(graph)
        self.visited = [0] * self.n
        
        for i in range(self.n):
            if self.visited[i] == 0:
                self.dfs(i)

        return [i for i in range(self.n) if self.visited[i] == 2]
