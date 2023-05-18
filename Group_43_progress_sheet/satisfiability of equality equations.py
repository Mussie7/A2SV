class Solution:
    def find(self, node):
        if self.rep[node] == node:
            return node
        
        # path compression
        self.rep[node] = self.find(self.rep[node])
        return self.rep[node]
    
    def union(self, node1, node2):
        rep1, rep2 = self.find(node1), self.find(node2)
        self.rep[rep1] = rep2

    def equationsPossible(self, equations: List[str]) -> bool:
        self.rep = {chr(ord('a') + i): chr(ord('a') + i) for i in range(26)}
        neg = []

        for var1, equal, _, var2 in equations:
            if equal == '!':
                neg.append([var1, var2])
            else:
                self.union(var1, var2)
        
        for var1, var2 in neg:
            if self.find(var1) == self.find(var2):
                return False
        return True
