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

    def removeStones(self, stones: List[List[int]]) -> int:
        for i in range(len(stones)):
            stones[i].append(i)

        def sort_union(flag):
            # sort it to get the same rows or the same columns together
            stones.sort(key=lambda x:x[flag])
            for i in range(len(stones) - 1):
                if stones[i][flag] == stones[i + 1][flag]:
                    self.union(stones[i][2], stones[i + 1][2])

        self.rep = [i for i in range(len(stones))]
        self.rank = [1] * len(stones)
        sort_union(0)
        sort_union(1)
        
        visited = set()
        removable = 0
        for i in range(len(stones)):
            rep = self.find(i)
            if rep not in visited:
                visited.add(rep)
                removable += self.rank[rep] - 1
        
        return removable
