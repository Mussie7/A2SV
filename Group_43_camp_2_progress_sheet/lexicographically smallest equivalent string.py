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
        
        if rep1 < rep2:
            self.rep[rep2] = rep1
        else:
            self.rep[rep1] = rep2

    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        self.rep = {chr(97 + i): chr(97 + i) for i in range(26)}
        n = len(s1)
        for i in range(n):
            self.union(s1[i], s2[i])
        
        smallestStr = []
        for char in baseStr:
            smallestStr.append(self.find(char))
        
        return ''.join(smallestStr)
