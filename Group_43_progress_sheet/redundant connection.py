class Solution:
    # recursive implementation
    def find(self, node):
        if node == self.rep[node]:
            return node

        self.rep[node] = self.find(self.rep[node])
        return self.rep[node]
    
    # iterative implementation
    def find_iter(self, node):
        root = node
        while self.rep[root] != root:
            root = self.rep[root]
        
        while node != self.rep[node]:
            self.rep[node], node = root, self.rep[node]
        
        return root
      
    def union(self, node1, node2):
        rep1 = self.find(node1)
        rep2 = self.find(node2)

        if rep1 == rep2:
            return False
        
        if self.rank[rep1] > self.rank[rep2]:
            self.rep[rep2] = rep1
            self.rank[rep1] += self.rank[rep2]
        else:
            self.rep[rep1] = rep2
            self.rank[rep2] += self.rank[rep1]
        
        return True

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        self.rep = [i for i in range(len(edges))]
        self.rank = [0] * len(edges)

        for parent, child in edges:
            if not self.union(parent-1, child-1):
                return [parent, child]
