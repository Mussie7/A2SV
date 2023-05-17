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


    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        self.rep = [i for i in range(n)]
        self.rank = [1] * n

        for node, neigh in edges:
            self.union(node, neigh)
        
        return self.find(source) == self.find(destination)
