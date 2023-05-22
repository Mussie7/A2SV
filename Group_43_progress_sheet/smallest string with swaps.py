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

    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        self.rep = [i for i in range(n)]
        self.rank = [1] * n

        for ind1, ind2 in pairs:
            self.union(ind1, ind2)
        
        rep_map = defaultdict(list)
        for ind in range(n):
            rep = self.find(ind)
            rep_map[rep].append(ind)
                
        smallest = [''] * n
        for rep in rep_map:
            rep_map[rep].sort()
            i = 0
            for char in sorted(rep_map[rep], key=lambda x: s[x]):
                smallest[rep_map[rep][i]] = s[char]
                i += 1
        
        return ''.join(smallest)
