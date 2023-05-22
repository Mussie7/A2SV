class Solution:
    def find(self, node):
        if self.rep[node] == node:
            return node
        # path compression
        self.rep[node] = self.find(self.rep[node])
        return self.rep[node]
    
    def union(self, node1, node2):
        rep1, rep2 = self.find(node1), self.find(node2)
        if rep1 == rep2:
            return
        # union by rank
        if self.rank[rep1] >= self.rank[rep2]:
            self.rep[rep2] = rep1
            self.rank[rep1] += self.rank[rep2]
        else:
            self.rep[rep1] = rep2
            self.rank[rep2] += self.rank[rep1]

    def minScore(self, n: int, roads: List[List[int]]) -> int:
        self.rep = [i for i in range(n + 1)]
        self.rank = [1] * (n + 1)
        
        min_path = defaultdict(lambda: inf)
        for city1, city2, dist in roads:
            path = min(min_path[self.find(city1)], min_path[self.find(city2)])
            self.union(city1, city2)

            rep = self.find(city1)
            min_path[rep] = min(path, dist)
        
        return min_path[self.find(1)]
