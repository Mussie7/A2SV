class Solution:
    def dfs(self, node, count):
        if self.visited[node][0]:
            if self.visited[node][0] == 2:
                return
            else:
                self.longest = max(self.longest, count - self.visited[node][1])
                return

        self.visited[node] = (1, count)
        if self.edges[node] != -1:
            self.dfs(self.edges[node], count + 1)
            
        self.visited[node] = (2,)

    def longestCycle(self, edges: List[int]) -> int:
        self.edges = edges
        self.visited = [(0,)] * len(self.edges)
        self.longest = -1
        for i in range(len(edges)):
            if self.visited[i][0] == 0:
                self.dfs(i, 1)
        
        return self.longest
