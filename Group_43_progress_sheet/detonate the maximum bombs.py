class Solution:
    def dfs(self, bomb):
        for casuality in self.graph[bomb]:
            if casuality not in self.visited:
                self.visited.add(casuality)
                self.dfs(casuality)

    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graph = defaultdict(list)
        for i in range(len(bombs)):
            x, y, r = bombs[i]
            for j in range(i+1, len(bombs)):
                x1, y1, r2 = bombs[j]
                dist = math.sqrt((x - x1) ** 2 + (y - y1) ** 2)
                if dist <= r:
                    graph[i].append(j)

                if dist <= r2:
                    graph[j].append(i)
        
        self.graph = graph
        max_detonation = 0
        for i in range(len(bombs)):
            self.visited = {i}
            self.dfs(i)
            max_detonation = max(len(self.visited), max_detonation)
        

        return max_detonation
