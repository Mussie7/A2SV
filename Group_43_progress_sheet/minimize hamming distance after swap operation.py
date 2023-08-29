class Solution:
    def find(self, node):
        if self.rep[node] == node:
            return node
        self.rep[node] = self.find(self.rep[node])
        return self.rep[node]
    
    def union(self, node1, node2):
        rep1, rep2 = self.find(node1), self.find(node2)
        if rep1 == rep2:
            return
        
        if self.rank[rep1] >= self.rank[rep2]:
            self.rep[rep2] = rep1
            self.rank[rep1] += self.rank[rep2]
        else:
            self.rep[rep1] = rep2
            self.rank[rep2] += self.rank[rep1]

    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        self.rep = list(range(n))
        self.rank = [1] * n

        for ind1, ind2 in allowedSwaps:
            self.union(ind1, ind2)
        
        rep_value_map = defaultdict(dict)
        for i in range(n):
            rep = self.find(i)
            if source[i] in rep_value_map[rep]:
                rep_value_map[rep][source[i]] += 1
            else:
                rep_value_map[rep][source[i]] = 1

            if target[i] in rep_value_map[rep]:
                rep_value_map[rep][target[i]] -= 1
            else:
                rep_value_map[rep][target[i]] = -1
        
        dist = 0
        for rep in rep_value_map:
            for value in rep_value_map[rep]:
                if rep_value_map[rep][value] > 0:
                    dist += rep_value_map[rep][value]
        
        return dist
