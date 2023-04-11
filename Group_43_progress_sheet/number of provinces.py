class Solution:
    def dfs(self, city):
        for neigh in self.graph[city]:
            if neigh not in self.visited:
                self.visited.add(neigh)
                self.dfs(neigh)

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        self.graph = defaultdict(list)
        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if i != j and isConnected[i][j] == 1:
                    self.graph[i].append(j)
        
        self.visited = set()
        province_count = 0
        for i in range(len(isConnected)):
            if i not in self.visited:
                province_count += 1
                self.visited.add(i)
                self.dfs(i)
        
        return province_count
      
      
      # better implementation with less space
    def dfs(self, city):
        for neigh, connected in enumerate(self.isConnected[city]):
            if connected and neigh not in self.visited:
                self.visited.add(neigh)
                self.dfs(neigh)

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        self.isConnected = isConnected
        self.visited = set()
        province_count = 0
        for i in range(len(isConnected)):
            if i not in self.visited:
                province_count += 1
                self.visited.add(i)
                self.dfs(i)
        
        return province_count
